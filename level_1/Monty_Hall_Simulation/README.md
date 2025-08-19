# Monty Hall Simulation

This project simulates the famous Monty Hall problem using Python and provides an interactive web interface with Streamlit.

## Project Overview

The Monty Hall problem is a probability puzzle based on a game show scenario. The player is presented with three doors: behind one is a car (the prize), and behind the other two are goats. After the player picks a door, the host (Monty) opens one of the remaining doors to reveal a goat. The player is then given the option to switch their choice to the other unopened door or stay with their original choice. This simulation demonstrates the probabilities of winning by switching or staying.

## Features
- Run multiple simulations to estimate probabilities
- Choose between "Switch" and "Stay" strategies
- Visualize results interactively with Streamlit

## How to Run

1. **Install dependencies:**
   ```bash
   pip install streamlit
   ```
2. **Run the Streamlit app:**
   ```bash
   streamlit run src/app.py
   ```
3. **Open the app in your browser** (usually at http://localhost:8501)

## Project Structure
- `src/app.py`: Streamlit web app for interactive simulation
- `src/main.py`: Core simulation logic
- `README.md`: Project documentation

## Example Output
The app displays the probability of winning a car or a goat based on the selected strategy and number of simulations.

## License
This project is for educational purposes.
