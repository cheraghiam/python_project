# Number Gusser

Number Gusser is a simple command-line game where you try to guess a randomly selected number between 1 and 100. The game provides feedback on whether your guess is too high or too low, and you can play as many rounds as you like!

![Number Gusser](images/number_gusser.jpg)

## How to Play

1. Run the game using Python:
    ```bash
    python src/condition_checker.py
    ```
2. Enter your guess (a number between 1 and 100) when prompted.
3. The game will tell you if your guess is too high or too low.
4. Each incorrect guess prompts you to guess again.
5. When you guess correctly, you can choose to play again or quit.

## Features
- Random number generation
- Continuous guessing until correct
- Replay option

## How to Run
```bash
export PYTHONPATH=$PYTHONPATH:`pwd`
python src/condition_checker.py
```

## Modules

### GameIO Module
Handles user input and random number generation.
- Prompts the user for guesses and validates input.
- Generates the target number for each round.

### condition_checker Module
Contains the logic to evaluate the user's guess.
- Checks if the guess is too high, too low, or correct.
- Provides feedback for each guess.
- Handles replay functionality.

## Educational Value
- Practice loops, conditionals, and random module
- User input validation
- Input validation and helpful prompts

## Example
Enter Your Guess Number: 50  
Your Number too Low!  
Enter Your Guess Number: 75  
Your Number too High!  
Enter Your Guess Number: 63  
Your Number too Low!  
Enter Your Guess Number: 70  
Congratulations! You've guessed the number 70.  
Do you want to play again? (yes/no): no  
Thank you for playing!

## License
This project is licensed under the MIT License.