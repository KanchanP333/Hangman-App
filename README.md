# Hangman-App
A classic word-guessing game implemented in Python with a clean command-line interface. 

🎮 Game Features

- Random Word Selection: Choose from a curated list of 1000+ English words
- Smart Word Filtering: Automatically excludes words with hyphens and spaces
- Lives System: Start with 6 lives and try to guess the word
- Input Validation: Handles duplicate guesses and invalid characters
- Visual Progress: See your guessed letters and current word progress
- Clean Interface: Clear feedback and game status updates

🚀 How to Play

- The game randomly selects a word from the word list
- You have 6 lives to guess the word correctly
- Guess one letter at a time
- Correct guesses reveal letter positions in the word
- Wrong guesses cost you a life
- Win by guessing all letters before running out of lives!

📋 Game Rules

✅ Enter single letters (A-Z)
❌ Repeated guesses don't count against you
🔄 Invalid inputs prompt you to try again
💀 Game ends when you run out of lives
🏆 Victory when all letters are guessed

🛠️ Installation & Setup

Running the Game

Clone the repository
```bash
git clone https://github.com/KanchanP333/hangman-game.git
cd hangman-game
```

Run the game
```bash
python hangman.py
```
🎯 Code Highlights

Set Operations: Utilizes Python sets for efficient letter tracking and validation
List Comprehension: Clean word display logic with dashes for unguessed letters
Random Selection: Fair word selection from extensive vocabulary

