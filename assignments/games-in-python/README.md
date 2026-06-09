
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a terminal-based Hangman game in Python to practice string manipulation, control flow, user input handling, and simple game state management.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Use the provided `starter-code.py` to implement a playable Hangman game. The program should run in the terminal and allow a single player to guess letters until they either reveal the secret word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from an internal list (use `random.choice`).
- Display the current progress to the player using underscores for unknown letters, e.g. `_ a _ g m a n`.
- Accept single-letter guesses (case-insensitive) and update the displayed progress.
- Track and display incorrect guesses remaining and list of letters already guessed.
- End the game and display a clear win or lose message.
- Be runnable with `python3 starter-code.py` and include a few example words in the starter list.

### 🛠️ Optional Extensions

#### Description
Add one or more extra features to make the game more complete or user-friendly. These are optional and meant for students who finish the core requirements early.

#### Requirements
Completed extension work may include one or more of the following:

- Allow guessing the full word as an input to win immediately.
- Add ASCII-art that updates as incorrect guesses accumulate.
- Support difficulty levels that change `max_incorrect` or the word list.
- Persist simple high scores or best times to a local file.

#### Notes
- Starter file: `starter-code.py` is provided to get started.
- Run locally with: `python3 starter-code.py`.

Good luck — have fun building Hangman! 🎮
