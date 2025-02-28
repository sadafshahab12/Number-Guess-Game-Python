# Guessing Game

## Description
This is a simple number guessing game where the player has 5 chances to guess a randomly generated number between 1 and 10. The game provides feedback after each guess to help guide the player toward the correct answer.

## How It Works
- The program generates a random number between 1 and 10.
- The player has 5 attempts to guess the correct number.
- After each incorrect guess:
  - The game informs the player if their guess is too high or too low.
  - If the player guesses correctly, the game congratulates them and ends.
  - If the player uses all 5 attempts without guessing correctly, the game reveals the correct number.

## How to Run
1. Ensure you have Python installed.
2. Copy the script into a Python file (e.g., `guessing_game.py`).
3. Run the script using the command:
   ```bash
   python guessing_game.py
   ```
4. Follow the on-screen instructions to play the game.

## Example Output
```
Guessing Game
You have 5 chances to guess the number
Guess from 1 to 10
Enter Your guess: 3
Your guess is very low, Try Again!
Enter Your guess: 7
Your guess is too high, Try Again!
Enter Your guess: 5
You guess the number 5 and You found it right! in the 3rd attempt
```

## Requirements
- Python 3.x

## Features
- Random number generation
- Limited attempts to guess
- Feedback on incorrect guesses
- Encouraging messages

## Future Enhancements
- Allow user to choose difficulty levels.
- Implement a scoring system.
- Add a replay option.

Enjoy playing the guessing game!
