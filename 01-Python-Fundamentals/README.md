# 01. Python Fundamentals — Guess the Number Game

## 📋 Overview

A terminal-based number-guessing game built in Python demonstrating core programming concepts: control structures, modular design, and data persistence.

**Features:**
- Single & two-player modes with configurable difficulty (Easy/Medium/Hard)
- Automatic game statistics tracking with Excel persistence
- 5 interactive visualization options (Matplotlib & Plotly)
- Clean modular architecture (4 focused modules)

---

## 📁 Repository Structure

```
01-Python-Fundamentals/
├── menu_principal.py       # Entry point & menu navigation
├── funciones_juego.py      # Core game logic (single/two-player, save results)
├── utilidades.py           # Helper functions (validation, data loading)
├── visualizaciones.py      # Statistics charts (pie, bar, tables)
├── TAREA.xlsx              # Game statistics database
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/NicolasSpector/master-data-science.git
cd master-data-science/01-Python-Fundamentals

# Install dependencies
pip install -r requirements.txt

# Play!
python menu_principal.py
```

---

## 🎮 How to Play

1. Select **game mode** (single-player, two-player, or view stats)
2. Choose **difficulty** (attempts: Easy=20, Medium=12, Hard=5)
3. Choose **range** (Easy=1-500, Medium=1-1000, Hard=1-5000)
4. **Guess the number** — hints provided after each attempt
5. Check **Statistics menu** for performance analysis

---

## 📚 Key Learnings

✅ **Control Structures** — `while` loops, `if/elif/else` for game logic and menu navigation  
✅ **Modular Programming** — Separation of concerns across 4 focused modules  
✅ **Data Persistence** — Reading/writing game results to Excel with `openpyxl` & `pandas`  
✅ **Data Visualization** — Multiple chart types (pie, bar, interactive tables) for statistical analysis  

---

## 📊 Statistics Dashboard

View your game history with 5 analysis options:
- General statistics by difficulty & game mode
- Per-player statistics (win rate, avg attempts)
- Player-specific performance
- Winners ranking
- Full game history table

---

<p align="center">
  <i>Part of <a href="../README.md">Master in Data Science Portfolio</a> · <a href="https://github.com/NicolasSpector">@NicolasSpector</a></i>
</p>
