![image](./images/password%20generator.jpg)
# Password Generator

A Python project for generating different types of passwords, including PINs, random passwords, and memorable passwords using English words.

## Features
- **PIN Password Generator**: Generates numeric PINs of customizable length.
- **Random Password Generator**: Generates passwords with letters, digits, and symbols, with customizable options.
- **Memorable Password Generator**: Generates passwords using random English words, with optional uppercase transformation for memorability.

## Requirements
- Python 3.x
- [nltk](https://www.nltk.org/) (Natural Language Toolkit)

## Installation
1. Clone the repository or download the source code.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main script to generate sample passwords:
```bash
python src/main.py
```

Example output:
```
PIN Password: 12345678
Random Password: aB3!xYz9@QwE
Memorable Password: TREE-dog-BOOK-apple
```

## Customization
You can customize the password length and options by editing the parameters in `src/main.py` or by importing the classes in your own scripts.

## Classes
- `PasswordGenerator`: Abstract base class for all password generators.
- `PinPasswordGenerator`: Generates numeric PINs.
- `RandomPasswordGenerator`: Generates random passwords with configurable character sets.
- `MemorablePasswordGenerator`: Generates memorable passwords using English words.

## Notes
- The memorable password generator uses the NLTK words corpus. The first run will download the word list automatically.
