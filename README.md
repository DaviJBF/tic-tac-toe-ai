# Tic-Tac-Toe AI

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A command-line Tic-Tac-Toe game where the AI is powered by the **Minimax algorithm**. The AI evaluates every possible move to ensure it plays optimally; it is mathematically impossible to beat this program.

---

## Requirements
* **Python 3.10 or higher**

To check your version, run:
```bash
# On Linux/macOS
python3 --version

# On Windows
python --version
```

## How to Run

*Note: In the execution commands below, use `python3` for Linux/macOS and `python` for Windows.*

### Option 1: Quick Download & Run
If you have curl installed, download and start the game:

**Linux / macOS / Windows CMD:**
```bash
curl -O [https://raw.githubusercontent.com/davijbf/tic-tac-toe-ai/main/src/main.py](https://raw.githubusercontent.com/davijbf/tic-tac-toe-ai/main/src/main.py) && python3 main.py
```

**Windows PowerShell:**
```powershell
curl -O [https://raw.githubusercontent.com/davijbf/tic-tac-toe-ai/main/src/main.py](https://raw.githubusercontent.com/davijbf/tic-tac-toe-ai/main/src/main.py); python main.py
```

### Option 2: Clone the Repo
```bash
git clone [https://github.com/davijbf/tic-tac-toe-ai.git](https://github.com/davijbf/tic-tac-toe-ai.git)
cd tic-tac-toe-ai

# On Linux/macOS
python3 src/main.py

# On Windows
python src\main.py
```

### Option 3: Manual Execution
Copy the code from `main.py` and paste it into an IDE (VS Code, PyCharm) or an online compiler like GDB Online.

## How to Play
* **Symbol Selection:** Choose 'X' or 'O'. Note that 'X' always moves first.
* **Coordinates:** Enter your move using the column letter (a, b, or c) followed by the row number (1, 2, or 3).

### Input Mapping

| | Column A | Column B | Column C |
| :--- | :---: | :---: | :---: |
| **Row 3** | a3 | b3 | c3 |
| **Row 2** | a2 | b2 | c2 |
| **Row 1** | a1 | b1 | c1 |

## Technical Overview
* **Algorithm:** Recursive Minimax.
* **UI:** Cross-platform CLI with automatic screen clearing (`cls` or `clear`).
* **Logic:** Algebraic coordinate mapping to 0-indexed list logic.