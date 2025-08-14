
# Number Gusser

Number Gusser is a simple command-line game where you try to guess a randomly selected number between 1 and 100. The game provides feedback on whether your guess is too high or too low, and you can play as many rounds as you like!

![Number Gusser](images/number_gusser.jpg)

## How to Play

1. Run the game using Python:
	```bash
	python src/main.py
	```
2. Enter your guess (a number between 1 and 100) when prompted.
3. The game will tell you if your guess is too high or too low.
4. Each incorrect guess reduces your score by 10 points.
5. Type `q` at any time to quit the game.
6. When you guess the correct number, your score is displayed and you can choose to play again or exit.

## Features
- Random number selection between 1 and 100
- Score tracking (starts at 100, -10 per wrong guess)
- Input validation and helpful prompts
- Option to play multiple rounds

## Requirements
- Python 3.x

## Example
```
Enter Your Number: 50
Your Number too Low
Enter Your Number: 75
Yourn Number too High
Enter Your Number: 63
Your Number too Low
Enter Your Number: 70
congratulations, your score: 70
Do you like play again:[y,n]: n
Good Bye...
```

## License
This project is licensed under the MIT License.
