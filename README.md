# ⚽ FIFA World Cup 2026 Score Tracking System

A Python-based **FIFA World Cup 2026 Score Tracking System** developed using **Tkinter** and **Object-Oriented Programming (OOP)**.

The system provides a graphical interface for recording football match results, automatically updating team standings, managing player squads, and viewing match statistics.

---

## 📌 Project Overview

The FIFA World Cup 2026 Score Tracking System was developed as a university programming project to demonstrate the practical use of **Python programming, Object-Oriented Programming, GUI development, and data management**.

The application allows users to:

* Record match results
* Automatically calculate team points
* Track wins, draws, and losses
* Calculate goals for, goals against, and goal difference
* View tournament standings
* Manage team squads
* Add and remove players
* View match history
* View tournament statistics

---

## 🛠️ Technologies Used

| Technology                     | Purpose                                          |
| ------------------------------ | ------------------------------------------------ |
| 🐍 Python                      | Main programming language                        |
| 🖥️ Tkinter                    | Graphical User Interface                         |
| 📦 Object-Oriented Programming | Organising teams, players, and application logic |
| 📋 ttk                         | Tables and GUI widgets                           |
| 📅 datetime                    | Recording match date and time                    |

---

## ✨ Features

### 🏆 Tournament Standings

The system automatically maintains a league table containing:

* Position
* Team
* Matches played
* Wins
* Draws
* Losses
* Goals scored
* Goals conceded
* Goal difference
* Points

Teams are automatically sorted according to their points, goal difference, and goals scored.

### ⚽ Match Entry

Users can enter:

* Home team
* Away team
* Home score
* Away score

The system then automatically determines whether the match resulted in:

* A home win
* An away win
* A draw

The relevant team statistics are updated automatically.

### 👥 Squad Management

The system allows users to manage team players.

Users can:

* View players
* Add players
* Delete players
* View player numbers
* View player positions
* Track player goals
* Track player assists

### 📝 Match Log

Every processed match is recorded in the match log with:

* Date and time
* Home team
* Home score
* Away team
* Away score
* Match result

### 📊 Tournament Statistics

The application provides an overview of tournament statistics, including:

* Number of teams
* Number of matches recorded
* Total goals scored
* Team wins
* Team draws

---

## 🌍 Teams Included

The current version includes:

* 🇿🇦 South Africa
* 🇲🇽 Mexico
* 🇰🇷 South Korea
* 🇨🇿 Czechia

The application can be expanded to include additional teams.

---

## 🏗️ Object-Oriented Design

The project demonstrates the use of classes in Python.

### `Player` Class

The `Player` class stores information about individual players.

It contains attributes such as:

```python
name
pos
number
goals
assists
```

### `Team` Class

The `Team` class stores information about each football team.

It manages:

```python
name
flag
played
wins
draws
losses
goals_for
goals_against
points
players
```

The class also calculates goal difference using:

```python
@property
def gd(self):
    return self.goals_for - self.goals_against
```

### `FIFA2026` Class

The main `FIFA2026` class controls the graphical interface and application functionality.

It manages:

* Navigation
* Standings
* Match entry
* Squad management
* Match logs
* Tournament statistics

---

## 🧮 Points System

The application uses the standard football points system:

| Match Result | Points |
| ------------ | -----: |
| 🟢 Win       |      3 |
| 🟡 Draw      |      1 |
| 🔴 Loss      |      0 |

For example, when a team wins:

```python
if hs > as_:
    h.points += 3
```

For a draw:

```python
else:
    h.points += 1
    a.points += 1
```

---

## 📂 Project Structure

```text
FIFA2026-Score-Tracking-System/
│
├── FIFA2026_Score_Tracking_System.py
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Install Python

Download and install Python from the official Python website.

Make sure Python is added to your system PATH during installation.

### 2. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 3. Open the Project Folder

```bash
cd FIFA2026-Score-Tracking-System
```

### 4. Run the Application

```bash
python FIFA2026_Score_Tracking_System.py
```

The FIFA World Cup 2026 Score Tracking System GUI should then open.

---

## 💻 Example Workflow

```text
Start Application
       │
       ▼
Select Match Entry
       │
       ▼
Select Home & Away Teams
       │
       ▼
Enter Match Score
       │
       ▼
Process Match
       │
       ▼
Update Team Statistics
       │
       ▼
Update Standings
       │
       ▼
Save Match to Log
```

---

## 📸 Screenshots

Screenshots of the application can be added here to demonstrate the graphical interface.

### Tournament Standings

*Add screenshot here*

### Match Entry

*Add screenshot here*

### Squad Management

*Add screenshot here*

### Match Log

*Add screenshot here*

---

## 🎓 Learning Outcomes

This project helped demonstrate practical understanding of:

* Python programming
* Object-Oriented Programming
* Classes and objects
* Functions and methods
* Conditional statements
* Lists and dictionaries
* GUI development with Tkinter
* Event-driven programming
* Data processing
* Input validation
* Basic software design
* User interface development

---

## 🚀 Future Improvements

Possible improvements include:

* Add all 2026 World Cup teams
* Add group-stage management
* Add knockout-stage management
* Add player goal and assist recording during matches
* Add team logos
* Add persistent database storage
* Add user login functionality
* Add export to CSV/PDF
* Add advanced tournament statistics
* Add match editing and deletion
* Add a more advanced graphical design
* Add online/cloud data storage

---

## ⚠️ Current Limitations

The current version stores tournament information in memory while the application is running.

Therefore, closing the application resets the recorded match results.

Future versions could use **SQLite or another database system** to permanently store the information.

---

## 👨‍💻 Project Type

**University Programming Project**

**Language:** Python
**GUI:** Tkinter
**Programming Approach:** Object-Oriented Programming
**Domain:** Football / Sports Management

---

## 📄 License

This project was created for educational and university project purposes.

---

## ⭐ Acknowledgement

This project was developed as part of a university programming project to demonstrate practical Python programming and software development skills.

If you find this project useful or interesting, feel free to ⭐ the repository.
