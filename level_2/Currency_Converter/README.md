![License](image/Currency.jpg)
# Currency Converter

A simple currency converter app that allows users to convert amounts between different currencies using real-time exchange rates.

## Features
- Real-time exchange rates fetched from [ExchangeRate-API](https://www.exchangerate-api.com/)
- Streamlit web interface for easy currency selection and conversion
- Command-line interface for quick conversions
- Jupyter notebook for testing and experimentation

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Install required Python packages:
   ```bash
   pip install streamlit requests
   ```

## Usage
### Streamlit App
Run the Streamlit app for a graphical interface:
```bash
streamlit run src/app.py
```

### Command-Line
Run the CLI tool:
```bash
python src/main.py
```
Follow the prompts to enter base and target currencies.

### Jupyter Notebook
Open `src/test.ipynb` for interactive testing and exploration.

## Project Structure
```
Currency_Converter/
├── src/
│   ├── app.py         # Streamlit web app
│   ├── main.py        # Command-line interface
│   ├── test.ipynb     # Jupyter notebook for testing
│   └── __pycache__/
├── README.md          # Project documentation
```

## License
This project is licensed under the MIT License.
