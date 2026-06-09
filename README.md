# Mini-Projects

![Python](https://img.shields.io/badge/python-3-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-games-00FF00?logo=pygame)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6B6B)
![Curses](https://img.shields.io/badge/Curses-terminal-000000)

> 20+ small Python projects across 5 domains. Games, GUIs, terminal tools, crypto utilities, and automation scripts. Built by following along a 14-hour Tech With Tim tutorial. Breadth over depth.

## What I Built It For

After the CV tutorial marathon came another one — 14 hours of Tech With Tim. Python projects from scratch. Games, utilities, GUIs, automation scripts. I followed along, typed every line, and by the end had 20+ projects in a single repo.

The variety was the point. Pygame for games. Tkinter for GUIs. Curses for terminal graphics. Cryptography for security. Subprocess for automation. Each project was small — 50 to 200 lines — but together they covered more of Python's ecosystem than any single large project could.

This was the tutorial that made me feel like Python was *mine*. Not just a language I was learning, but a tool I could pick up and build anything with.

## Project Summary

| Domain | Projects | Key Technologies |
|--------|----------|-----------------|
| 🎮 Pygame Games | 4 | Pygame, pygame.mixer, random, math |
| 🖥️ tkinter GUIs | 2 | Tkinter, filedialog, pytube |
| ⌨️ Curses CLI Tools | 3 | curses, BFS pathfinding, WPM tracking |
| 🔐 Crypto & Utilities | 6 | Fernet encryption, pickle, pickle, shutil, schedule |
| ⚙️ Automation & Hardware | 5+ | subprocess, pygame.joystick, os.walk, Go compilation |

---

## 🎮 Pygame Games

### Aim Trainer (`aim_trainer.py`) — 193 lines
Target shooting game. Circles appear randomly on screen, growing and shrinking over time. Tracks hits, misses, speed (targets/second), and accuracy. Features sound effects for hits and misses, and an end-game stats screen. Uses `pygame.mixer` for audio.

### Turtle Racing (`Turtle.py`) — 64 lines
Bet on colorful turtles racing across the screen. Uses Python's built-in `turtle` module. Configurable number of racers (2-10), random speeds, winner detection.

### Slot Machine (`Slot Machine (M).py`) — 149 lines
Casino-style slot machine simulator. 3x3 grid with weighted symbols (A/B/C/D), configurable bet lines (1-3), balance tracking, win calculation with symbol values.

### PS4 Controller Visualizer (`Controller/controller.py`) — 115 lines
Real-time Pygame visualization of PS4 controller input. Renders analog stick positions as circles, trigger values as bars, and button states as colored labels. Useful for testing controller mappings.

**Setup:**
```bash
pip install pygame
python aim_trainer.py
```

---

## 🖥️ tkinter GUIs

### YouTube Downloader (`youtube_download.py`) — 88 lines
Downloads YouTube videos at user-specified resolution using `pytube`. Features a Tkinter folder picker dialog for save location and a progress callback showing download percentage in real time.

### Madlibs Generator (`madlibs generator/main.py`) — 42 lines
Reads a story template with `<placeholder>` tags, prompts the user for words, and fills them in. Simple but effective demonstration of string parsing and user input collection.

**Setup:**
```bash
pip install pytube
python youtube_download.py
python madlibs\ generator/main.py
```

---

## ⌨️ Curses CLI Tools

### BFS Maze Path Finder (`path_finder.py`) — 145 lines
Breadth-First Search pathfinding visualizer rendered in the terminal using `curses`. A 19×19 maze with walls (#), start point (O), and end point (X). The algorithm animates the search in real time — blue for visited nodes, red for the final solution path. Uses `queue` for BFS frontier management.

### Typing Speed Test (`typing test/typing_test.py`) — 78 lines
Terminal-based typing speed test. Displays target text, tracks WPM in real time as you type, highlights correct/incorrect characters with color. Uses `curses` for live terminal rendering and `random` for text selection.

### Rock Paper Scissors (`rock_paper.py`) — 39 lines
Classic CLI game. Tracks user vs computer wins across rounds. Simple but polished — input validation, score tracking, quit option.

**Setup:**
```bash
# Curses is built into Python on Linux/Mac. On Windows:
pip install windows-curses
python path_finder.py
```

---

## 🔐 Crypto & Utilities

### Password Manager (`password_manager.py/password_manager.py`) — 57 lines
Encrypted password storage using `cryptography.fernet` (Fernet symmetric encryption). Passwords are persisted via `pickle` to a text file, encrypted with a key file. Supports add, view, and delete operations. Master password protected.

### Password Generator (`pass_gen.py`) — 46 lines
Generates random secure passwords with configurable length, numbers, and special characters. Uses `string` module for character sets. Ensures generated passwords meet all criteria before returning.

### File Backup (`file backup/file_backup.py`) — 34 lines
Automated file backup utility using `schedule` for periodic execution. Copies a source directory to dated backup folders using `shutil.copytree`. Originally configured for screenshot backups.

### Alarm Clock (`alarm clock/alarm clock.py`) — 44 lines
Countdown timer that plays an MP3 alarm sound when time expires. Uses `playsound` for audio playback. Terminal-based with live countdown display.

### Number Guessing Game (`number_guess.py`) — 34 lines
Classic guess-the-number game. Configurable range, tracks number of attempts, gives higher/lower hints.

### Time Math Challenge (`time math challenge.py`)
Math quiz against the clock. Generates random arithmetic problems, times the user's responses.

### MasterMind Game (`MasterMindGame.py`) — 75 lines
Code-breaking logic game. Player guesses a 4-color code from 6 possible colors (R/G/B/Y/W/O). Feedback shows correct position+color and correct color but wrong position. 10 attempts to crack the code.

**Setup:**
```bash
pip install cryptography schedule playsound
python password_manager.py/password_manager.py
```

---

## ⚙️ Automation & Hardware

### Py Scripting (`Py Scripting/`) — Script.py (121 lines)
Automation sub-project that finds Go game directories, compiles them, and generates metadata. Uses `os.walk` for directory traversal, `subprocess.run` for Go compilation, and `json` for metadata output. Includes sample game data (spider game, Simon Says, rock-paper-scissors, hello world) with pre-compiled `.exe` files.

### PS4 Controller Module (`Controller/controller_module.py`) — 114 lines
Reusable Python module for reading PS4 controller input. Reads all 6 axes (left stick X/Y, right stick X/Y, L2/R2 triggers) and all buttons. Built on `pygame.joystick`. Designed as an importable module for use in other projects.

### Dual Controller (`Controller/controller-single.py`)
Standalone script variant of the controller module for single-controller setups.

**Setup:**
```bash
pip install pygame
# Controller requires a physical PS4 controller connected via USB/Bluetooth
python Controller/controller.py

# Py Scripting requires Go installed
python Py\ Scripting/Script.py
```

---

## Quick Reference — All Projects

| # | Project | File | Domain | Lines |
|---|---------|------|--------|-------|
| 1 | Aim Trainer | `aim_trainer.py` | Pygame | 193 |
| 2 | BFS Maze Solver | `path_finder.py` | Curses | 145 |
| 3 | Slot Machine | `Slot Machine (M).py` | Pygame | 149 |
| 4 | PS4 Visualizer | `Controller/controller.py` | Pygame | 115 |
| 5 | Controller Module | `Controller/controller_module.py` | Hardware | 114 |
| 6 | YouTube Downloader | `youtube_download.py` | Tkinter | 88 |
| 7 | Typing Test | `typing test/typing_test.py` | Curses | 78 |
| 8 | MasterMind | `MasterMindGame.py` | CLI | 75 |
| 9 | Turtle Racing | `Turtle.py` | Turtle | 64 |
| 10 | Password Manager | `password_manager.py/` | Crypto | 57 |
| 11 | Password Generator | `pass_gen.py` | Crypto | 46 |
| 12 | Alarm Clock | `alarm clock/alarm clock.py` | Utility | 44 |
| 13 | Madlibs Generator | `madlibs generator/main.py` | Tkinter | 42 |
| 14 | Rock Paper Scissors | `rock_paper.py` | CLI | 39 |
| 15 | File Backup | `file backup/file_backup.py` | Utility | 34 |
| 16 | Number Guessing | `number_guess.py` | CLI | 34 |
| 17 | Time Math Challenge | `time math challenge.py` | CLI | — |
| 18 | Py Scripting | `Py Scripting/Script.py` | Automation | 121 |

## Project Structure

```
Mini-Projects/
├── aim_trainer.py                 # 🎮 Pygame target shooting game
├── path_finder.py                 # ⌨️ BFS maze solver (curses)
├── Slot Machine (M).py            # 🎮 Casino slot machine
├── Turtle.py                      # 🎮 Turtle racing game
├── MasterMindGame.py              # 🔐 Code-breaking logic game
├── rock_paper.py                  # ⌨️ Rock paper scissors
├── number_guess.py                # ⌨️ Number guessing game
├── time math challenge.py         # ⌨️ Math quiz
├── pass_gen.py                    # 🔐 Password generator
├── youtube_download.py            # 🖥️ YouTube downloader (tkinter)
├── OhMyPosh Setup.bat             # ⚙️ Terminal theme setup
│
├── Controller/                    # 🎮 PS4 controller interface
│   ├── controller_module.py       #    Reusable input module
│   ├── controller.py              #    Dual-controller visualizer
│   └── controller-single.py       #    Single-controller variant
│
├── password_manager.py/           # 🔐 Encrypted password storage
│   ├── password_manager.py
│   ├── password.txt
│   └── key.key
│
├── typing test/                   # ⌨️ Speed typing test
│   ├── typing_test.py
│   └── text.txt
│
├── alarm clock/                   # 🔐 Alarm clock utility
│   ├── alarm clock.py
│   └── alarm.mp3
│
├── file backup/                   # 🔐 Automated file backup
│   └── file_backup.py
│
├── madlibs generator/             # 🖥️ Madlibs word game
│   ├── main.py
│   └── story.txt
│
├── sounds/                        # 🎮 Shared audio assets
│   ├── target_hit.mp3
│   ├── misclick.mp3
│   └── fail_target.mp3
│
└── Py Scripting/                  # ⚙️ Go compilation automation
    ├── Script.py
    ├── data/                      #    Source game data
    ├── new_data/                  #    Compiled outputs
    └── Python-Scripting-Project-main/
        ├── get_game_data.py
        └── project.txt
```

## Tech Stack Summary

| Technology | Used In |
|-----------|---------|
| Pygame | Aim Trainer, Slot Machine, PS4 Visualizer |
| pygame.joystick | Controller module, PS4 Visualizer |
| pygame.mixer | Aim Trainer (sound effects) |
| curses | BFS Maze Solver, Typing Test |
| Tkinter | YouTube Downloader (folder picker) |
| turtle | Turtle Racing |
| cryptography (Fernet) | Password Manager |
| pickle | Password Manager, File Backup |
| pytube | YouTube Downloader |
| playsound | Alarm Clock |
| schedule | File Backup |
| shutil | File Backup |
| subprocess | Py Scripting (Go compilation) |
| os.walk | Py Scripting |

## Timeline

- **Aug 27, 2024** — Initial commit
- **Aug–Sep 2024** — Core games and utilities added (5 commits)
- **Jan 13, 2025** — Final additions (controller module, YouTube downloader)
- **7 commits total** over 5 months of iterative additions

---

Built by following along. Kept because every project taught something different.
