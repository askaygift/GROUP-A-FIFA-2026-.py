import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class Player:
    def __init__(self, name, pos, number):
        self.name = name
        self.pos = pos
        self.number = number
        self.goals = 0
        self.assists = 0


class Team:
    def __init__(self, name, flag=""):
        self.name = name
        self.flag = flag
        self.played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0
        self.players = []

    @property
    def gd(self):
        return self.goals_for - self.goals_against


TEAMS = {}
MATCH_LOG = []


def init_squads():
    """Create the teams and a small starting squad for each team."""
    global TEAMS

    TEAMS = {
        "South Africa": Team("South Africa", "🇿🇦"),
        "Mexico": Team("Mexico", "🇲🇽"),
        "South Korea": Team("South Korea", "🇰🇷"),
        "Czechia": Team("Czechia", "🇨🇿"),
    }

    squads = {
        "South Africa": [
            ("Ronwen Williams", "GK", 1),
            ("Teboho Mokoena", "MID", 4),
            ("Percy Tau", "FWD", 10),
            ("Evidence Makgopa", "FWD", 9),
        ],
        "Mexico": [
            ("Luis Malagon", "GK", 1),
            ("Edson Alvarez", "MID", 4),
            ("Hirving Lozano", "FWD", 22),
            ("Raul Jimenez", "FWD", 9),
        ],
        "South Korea": [
            ("Kim Seung-gyu", "GK", 1),
            ("Lee Kang-in", "MID", 18),
            ("Son Heung-min", "FWD", 7),
            ("Hwang Hee-chan", "FWD", 11),
        ],
        "Czechia": [
            ("Jindrich Stanek", "GK", 1),
            ("Tomas Soucek", "MID", 22),
            ("Adam Hlozek", "FWD", 9),
            ("Patrik Schick", "FWD", 10),
        ],
    }

    for team_name, players in squads.items():
        for name, position, number in players:
            TEAMS[team_name].players.append(Player(name, position, number))


class FIFA2026(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("FIFA World Cup 2026 Score Tracking System")
        self.geometry("1050x700")
        self.minsize(900, 600)

        self.configure(bg="#f2f2f2")

        init_squads()

        self._build()
        self._show("Standings")
        self._refresh_table()
        self._refresh_squad()
        self._refresh_log()

    def _build(self):
        """Build the main application window."""
        header = tk.Frame(self, bg="#202a44", height=70)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="FIFA WORLD CUP 2026",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#202a44",
        )
        title.pack(side="left", padx=25, pady=15)

        subtitle = tk.Label(
            header,
            text="Score Tracking System",
            font=("Arial", 11),
            fg="#d9e2f3",
            bg="#202a44",
        )
        subtitle.pack(side="left", padx=5, pady=18)

        nav = tk.Frame(self, bg="#dfe5f2", height=50)
        nav.pack(fill="x")

        buttons = [
            ("Standings", "Standings"),
            ("Match Entry", "Match Entry"),
            ("Squads", "Squads"),
            ("Log", "Log"),
        ]

        for text, page in buttons:
            tk.Button(
                nav,
                text=text,
                command=lambda p=page: self._show(p),
                font=("Arial", 10, "bold"),
                relief="flat",
                padx=18,
                pady=8,
                bg="white",
            ).pack(side="left", padx=5, pady=7)

        self.container = tk.Frame(self, bg="#f2f2f2")
        self.container.pack(fill="both", expand=True, padx=15, pady=15)

        self.pages = {}
        self._init_table_ui()
        self._init_match_ui()
        self._init_squad_ui()
        self._init_log_ui()

    def _show(self, page):
        """Show one application page."""
        for frame in self.pages.values():
            frame.pack_forget()

        self.pages[page].pack(fill="both", expand=True)

        if page == "Standings":
            self._refresh_table()
        elif page == "Squads":
            self._refresh_squad()
        elif page == "Log":
            self._refresh_log()

    def _init_table_ui(self):
        frame = tk.Frame(self.container, bg="white", bd=1, relief="solid")
        self.pages["Standings"] = frame

        tk.Label(
            frame,
            text="Tournament Standings",
            font=("Arial", 18, "bold"),
            bg="white",
        ).pack(anchor="w", padx=20, pady=(20, 10))

        tk.Label(
            frame,
            text="Teams are automatically updated after each match.",
            font=("Arial", 10),
            fg="#555555",
            bg="white",
        ).pack(anchor="w", padx=20, pady=(0, 15))

        columns = (
            "pos",
            "team",
            "played",
            "wins",
            "draws",
            "losses",
            "gf",
            "ga",
            "gd",
            "points",
        )

        self.table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=15,
        )

        headings = {
            "pos": "#",
            "team": "Team",
            "played": "P",
            "wins": "W",
            "draws": "D",
            "losses": "L",
            "gf": "GF",
            "ga": "GA",
            "gd": "GD",
            "points": "Pts",
        }

        widths = {
            "pos": 50,
            "team": 220,
            "played": 70,
            "wins": 70,
            "draws": 70,
            "losses": 70,
            "gf": 70,
            "ga": 70,
            "gd": 70,
            "points": 80,
        }

        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=widths[col], anchor="center")

        self.table.column("team", anchor="w")
        self.table.pack(fill="x", padx=20, pady=10)

    def _refresh_table(self):
        if not hasattr(self, "table"):
            return

        for item in self.table.get_children():
            self.table.delete(item)

        teams = sorted(
            TEAMS.values(),
            key=lambda t: (t.points, t.gd, t.goals_for),
            reverse=True,
        )

        for position, team in enumerate(teams, start=1):
            self.table.insert(
                "",
                "end",
                values=(
                    position,
                    f"{team.flag} {team.name}",
                    team.played,
                    team.wins,
                    team.draws,
                    team.losses,
                    team.goals_for,
                    team.goals_against,
                    team.gd,
                    team.points,
                ),
            )

    def _init_match_ui(self):
        frame = tk.Frame(self.container, bg="white", bd=1, relief="solid")
        self.pages["Match Entry"] = frame

        tk.Label(
            frame,
            text="Enter Match Result",
            font=("Arial", 18, "bold"),
            bg="white",
        ).pack(anchor="w", padx=20, pady=(20, 5))

        tk.Label(
            frame,
            text="Enter the teams and final score. The standings will update automatically.",
            font=("Arial", 10),
            fg="#555555",
            bg="white",
        ).pack(anchor="w", padx=20, pady=(0, 20))

        form = tk.Frame(frame, bg="white")
        form.pack(pady=20)

        tk.Label(form, text="Home Team:", font=("Arial", 11, "bold"), bg="white").grid(
            row=0, column=0, padx=10, pady=12, sticky="e"
        )

        self.home_var = tk.StringVar()
        self.home_combo = ttk.Combobox(
            form,
            textvariable=self.home_var,
            values=list(TEAMS.keys()),
            state="readonly",
            width=25,
        )
        self.home_combo.grid(row=0, column=1, padx=10, pady=12)

        tk.Label(form, text="Home Score:", font=("Arial", 11, "bold"), bg="white").grid(
            row=0, column=2, padx=10, pady=12, sticky="e"
        )

        self.home_score_var = tk.StringVar()
        tk.Entry(
            form,
            textvariable=self.home_score_var,
            width=8,
            justify="center",
        ).grid(row=0, column=3, padx=10, pady=12)

        tk.Label(form, text="Away Team:", font=("Arial", 11, "bold"), bg="white").grid(
            row=1, column=0, padx=10, pady=12, sticky="e"
        )

        self.away_var = tk.StringVar()
        self.away_combo = ttk.Combobox(
            form,
            textvariable=self.away_var,
            values=list(TEAMS.keys()),
            state="readonly",
            width=25,
        )
        self.away_combo.grid(row=1, column=1, padx=10, pady=12)

        tk.Label(form, text="Away Score:", font=("Arial", 11, "bold"), bg="white").grid(
            row=1, column=2, padx=10, pady=12, sticky="e"
        )

        self.away_score_var = tk.StringVar()
        tk.Entry(
            form,
            textvariable=self.away_score_var,
            width=8,
            justify="center",
        ).grid(row=1, column=3, padx=10, pady=12)

        tk.Button(
            frame,
            text="PROCESS MATCH",
            command=self._process_match,
            font=("Arial", 11, "bold"),
            padx=25,
            pady=10,
        ).pack(pady=20)

        self.result_label = tk.Label(
            frame,
            text="",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#202a44",
        )
        self.result_label.pack(pady=10)

    def _process_match(self):
        """Validate and process a match result."""
        home_name = self.home_var.get()
        away_name = self.away_var.get()

        if not home_name or not away_name:
            messagebox.showwarning(
                "Missing Teams",
                "Please select both the home and away teams.",
            )
            return

        if home_name == away_name:
            messagebox.showwarning(
                "Invalid Match",
                "A team cannot play against itself.",
            )
            return

        try:
            hs = int(self.home_score_var.get())
            as_ = int(self.away_score_var.get())

            if hs < 0 or as_ < 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Score",
                "Please enter valid non-negative whole numbers for both scores.",
            )
            return

        h = TEAMS[home_name]
        a = TEAMS[away_name]

        h.played += 1
        a.played += 1

        h.goals_for += hs
        h.goals_against += as_

        a.goals_for += as_
        a.goals_against += hs

        if hs > as_:
            h.wins += 1
            a.losses += 1
            h.points += 3
            result = f"{home_name} won {hs} - {as_}"
        elif as_ > hs:
            a.wins += 1
            h.losses += 1
            a.points += 3
            result = f"{away_name} won {as_} - {hs}"
        else:
            h.draws += 1
            a.draws += 1
            h.points += 1
            a.points += 1
            result = f"{home_name} and {away_name} drew {hs} - {as_}"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        MATCH_LOG.append(
            {
                "time": timestamp,
                "home": home_name,
                "home_score": hs,
                "away": away_name,
                "away_score": as_,
                "result": result,
            }
        )

        self.result_label.config(text=result)
        self.home_score_var.set("")
        self.away_score_var.set("")

        self._refresh_table()
        self._refresh_log()

        messagebox.showinfo(
            "Match Processed",
            f"{result}\n\nThe standings have been updated.",
        )

    def _init_squad_ui(self):
        frame = tk.Frame(self.container, bg="white", bd=1, relief="solid")
        self.pages["Squads"] = frame

        tk.Label(
            frame,
            text="Team Squads",
            font=("Arial", 18, "bold"),
            bg="white",
        ).pack(anchor="w", padx=20, pady=(20, 5))

        controls = tk.Frame(frame, bg="white")
        controls.pack(fill="x", padx=20, pady=10)

        tk.Label(
            controls,
            text="Select Team:",
            font=("Arial", 10, "bold"),
            bg="white",
        ).pack(side="left", padx=(0, 8))

        self.squad_team_var = tk.StringVar()
        self.squad_combo = ttk.Combobox(
            controls,
            textvariable=self.squad_team_var,
            values=list(TEAMS.keys()),
            state="readonly",
            width=25,
        )
        self.squad_combo.pack(side="left")
        self.squad_combo.bind("<<ComboboxSelected>>", lambda event: self._refresh_squad())

        tk.Button(
            controls,
            text="Add Player",
            command=self._add_p_pop,
        ).pack(side="left", padx=10)

        tk.Button(
            controls,
            text="Delete Selected",
            command=self._del_p,
        ).pack(side="left", padx=5)

        columns = ("number", "name", "position", "goals", "assists")

        self.squad_table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=14,
        )

        headings = {
            "number": "No.",
            "name": "Player Name",
            "position": "Position",
            "goals": "Goals",
            "assists": "Assists",
        }

        for col in columns:
            self.squad_table.heading(col, text=headings[col])
            self.squad_table.column(col, anchor="center", width=120)

        self.squad_table.column("name", width=260, anchor="w")
        self.squad_table.pack(fill="x", padx=20, pady=15)

        if TEAMS:
            self.squad_team_var.set(next(iter(TEAMS)))

    def _refresh_squad(self):
        if not hasattr(self, "squad_table"):
            return

        for item in self.squad_table.get_children():
            self.squad_table.delete(item)

        team_name = self.squad_team_var.get()

        if not team_name or team_name not in TEAMS:
            return

        team = TEAMS[team_name]

        for player in team.players:
            self.squad_table.insert(
                "",
                "end",
                values=(
                    player.number,
                    player.name,
                    player.pos,
                    player.goals,
                    player.assists,
                ),
            )

    def _add_p_pop(self):
        """Open a small form for adding a player."""
        team_name = self.squad_team_var.get()

        if not team_name:
            messagebox.showwarning("No Team", "Please select a team first.")
            return

        win = tk.Toplevel(self)
        win.title("Add Player")
        win.geometry("380x300")
        win.resizable(False, False)
        win.grab_set()

        tk.Label(
            win,
            text=f"Add Player to {team_name}",
            font=("Arial", 14, "bold"),
        ).pack(pady=15)

        form = tk.Frame(win)
        form.pack(pady=10)

        tk.Label(form, text="Name:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
        name_entry = tk.Entry(form, width=25)
        name_entry.grid(row=0, column=1, padx=8, pady=8)

        tk.Label(form, text="Position:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
        pos_combo = ttk.Combobox(
            form,
            values=["GK", "DEF", "MID", "FWD"],
            state="readonly",
            width=22,
        )
        pos_combo.grid(row=1, column=1, padx=8, pady=8)
        pos_combo.set("MID")

        tk.Label(form, text="Number:").grid(row=2, column=0, padx=8, pady=8, sticky="e")
        number_entry = tk.Entry(form, width=25)
        number_entry.grid(row=2, column=1, padx=8, pady=8)

        def save_player():
            name = name_entry.get().strip()
            position = pos_combo.get().strip()

            try:
                number = int(number_entry.get())
            except ValueError:
                messagebox.showerror("Invalid Number", "Player number must be a whole number.")
                return

            if not name:
                messagebox.showwarning("Missing Name", "Please enter the player's name.")
                return

            if number < 1:
                messagebox.showwarning("Invalid Number", "Player number must be greater than 0.")
                return

            TEAMS[team_name].players.append(Player(name, position, number))
            self._refresh_squad()
            win.destroy()

        tk.Button(
            win,
            text="Save Player",
            command=save_player,
            padx=20,
            pady=8,
        ).pack(pady=15)

    def _del_p(self):
        """Delete the selected player from the selected team."""
        team_name = self.squad_team_var.get()

        if not team_name:
            messagebox.showwarning("No Team", "Please select a team.")
            return

        selected = self.squad_table.selection()

        if not selected:
            messagebox.showwarning(
                "No Player Selected",
                "Please select a player to delete.",
            )
            return

        item = self.squad_table.item(selected[0])
        player_number = item["values"][0]

        team = TEAMS[team_name]

        for index, player in enumerate(team.players):
            if player.number == player_number:
                del team.players[index]
                break

        self._refresh_squad()

    def _stat_window(self):
        """Display a summary of tournament statistics."""
        total_matches = len(MATCH_LOG)
        total_goals = sum(
            team.goals_for for team in TEAMS.values()
        )

        win_counts = sum(team.wins for team in TEAMS.values())
        draw_counts = sum(team.draws for team in TEAMS.values())

        messagebox.showinfo(
            "Tournament Statistics",
            f"Teams: {len(TEAMS)}\n"
            f"Matches recorded: {total_matches}\n"
            f"Goals scored: {total_goals}\n"
            f"Team wins recorded: {win_counts}\n"
            f"Team draws recorded: {draw_counts}",
        )

    def _init_log_ui(self):
        frame = tk.Frame(self.container, bg="white", bd=1, relief="solid")
        self.pages["Log"] = frame

        top = tk.Frame(frame, bg="white")
        top.pack(fill="x", padx=20, pady=(20, 10))

        tk.Label(
            top,
            text="Match Log",
            font=("Arial", 18, "bold"),
            bg="white",
        ).pack(side="left")

        tk.Button(
            top,
            text="Tournament Statistics",
            command=self._stat_window,
        ).pack(side="right")

        columns = (
            "time",
            "home",
            "score",
            "away",
            "result",
        )

        self.log_table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=16,
        )

        headings = {
            "time": "Date / Time",
            "home": "Home Team",
            "score": "Score",
            "away": "Away Team",
            "result": "Result",
        }

        widths = {
            "time": 160,
            "home": 170,
            "score": 90,
            "away": 170,
            "result": 280,
        }

        for col in columns:
            self.log_table.heading(col, text=headings[col])
            self.log_table.column(col, width=widths[col], anchor="center")

        self.log_table.pack(fill="both", expand=True, padx=20, pady=10)

    def _refresh_log(self):
        if not hasattr(self, "log_table"):
            return

        for item in self.log_table.get_children():
            self.log_table.delete(item)

        for match in reversed(MATCH_LOG):
            self.log_table.insert(
                "",
                "end",
                values=(
                    match["time"],
                    match["home"],
                    f"{match['home_score']} - {match['away_score']}",
                    match["away"],
                    match["result"],
                ),
            )


if __name__ == "__main__":
    app = FIFA2026()
    app.mainloop()
