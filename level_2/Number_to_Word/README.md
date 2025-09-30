# Number to Word

A simple Python project that converts numbers (below 100) into their English word representation.

## Features

- Converts numbers from 0 to 99 into words
- Easy-to-use function interface
- Includes a testable script and Jupyter notebook for experimentation

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:cheraghiam/python_project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Number_to_Word
   ```

## Usage

### Command-Line

Run the main script to see example conversions:
```bash
export PYTHON=`pwd`
python src/main.py
```

### As a Module

```bash
export PYTHON=`pwd`
You can import and use the function in your own code:
```python
from src.main import Num2Word

print(Num2Word(42))  # Output: forty two
```

### Jupyter Notebook

Open `src/test.ipynb` for interactive testing and exploration.

## Project Structure

```
Number_to_Word/
├── src/
│   ├── constant.py   # Dictionaries for number-word mapping
│   ├── main.py       # Main conversion logic and CLI
│   ├── test.ipynb    # Jupyter notebook for testing
│   └── __pycache__/
├── README.md         # Project documentation
```

## License

This project is licensed under the MIT License.