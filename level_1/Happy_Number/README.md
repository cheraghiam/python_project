## Happy Number Checker

This project provides a simple Python script to check whether a given number is a **happy number**.

### What is a Happy Number?
A happy number is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
3. Numbers for which this process ends in 1 are called **happy numbers**.

### Example
For example, 7 is a happy number:
```
7 → 49 → 97 → 130 → 10 → 1
```

### How to Use
1. Make sure you have Python installed (version 3.x).
2. Run the script:
	```bash
	python src/main.py
	```
3. Enter a number when prompted. The script will tell you if your number is happy or not.

### Code Overview
- `happy_number(n: int) -> bool`: Checks if a number is happy.
- `input_user_number() -> int`: Prompts the user for input and validates it.
- The script runs interactively if executed directly.

---
*Author: amirabbas*
