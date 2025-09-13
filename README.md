# 🧠 Brain Training App/Game (CLI Version)

Welcome to the **Brain Training App** — a modular and expandable collection of mini-games designed to **boost your memory, logic, math skills, and reaction time**.  
Built in **Python**, this project is perfect for **learning + fun**. 🎉

---

## 🎮 Mini-Games Available

1. **💭 Memory Game**  
   - Remember a number shown for a few seconds.  
   - Type it back correctly to progress.  
   - Numbers get longer each round, time gets shorter.  

2. **⚡ Reaction Time Game**  
   - Wait for `GO!`  
   - Hit **Enter** as fast as possible.  
   - Shows **average** and **best** reaction times.  

---

## 📂 Project Structure

```
brain_training/
│
├── main.py                  # 🎯 Game launcher / menu
├── memory_game.py           # 💭 Memory test game
├── reaction_game.py         # ⚡ Reaction timer game
├── stats.py                 # 📊 Stats & performance tracking
├── utils.py                 # 🛠️ Common utilities
│
├── data/
│   └── scores.json          # 📁 Stored stats & high scores
│
└── assets/
    └── instructions.txt     # 📜 Help / instructions
```

---

## ▶️ How to Play

### 1. Clone or Download
Download the ZIP and extract, or clone via git:
```bash
git clone https://github.com/your-username/brain_training.git
cd brain_training
```

### 2. Run the App
```bash
python3 main.py
```

### 3. Main Menu Options
When you start, you’ll see:

```
========================================
   🧠 Brain Training — CLI Launcher
========================================
1) Memory Game (Number Memory)
2) Reaction Time Game
3) View Stats
4) Reset Stats
0) Exit
========================================
Choose (0-4):
```

- **Option 1:** Start Memory Game  
- **Option 2:** Start Reaction Time Game  
- **Option 3:** View saved stats  
- **Option 4:** Reset all stats  
- **Option 0:** Exit  

---

## 📊 Stats Tracking

- Game results are saved automatically in:  
  **`data/scores.json`**
- Tracks:  
  - High scores  
  - Levels reached  
  - Best reaction times  
  - Games played  

Example stats file:
```json
{
  "memory_game": {
    "high_score": 5,
    "games_played": 3,
    "max_levels": 5
  },
  "reaction_game": {
    "best_reaction": 0.289,
    "games_played": 4,
    "last_avg_reaction": 0.412
  }
}
```

---

## 🚀 Future Features

- 🧮 Math challenges (quick arithmetic)  
- 🧩 Logic puzzles (odd-one-out, pattern matching)  
- 🔒 User profiles  
- 🌐 Online scoreboard  
- 🎵 Sound effects & animations  

---

## 💡 Why This Project?

✔ Beginner-friendly Python project  
✔ Learn **JSON, modules, game logic**  
✔ Expandable with new mini-games  
✔ Fun way to train your brain daily!  

---

✨ **Keep training your brain — Have fun coding & playing!**
