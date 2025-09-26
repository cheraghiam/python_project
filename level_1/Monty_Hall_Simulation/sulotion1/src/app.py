import streamlit as st
from src.main import counter_simulation


st.image("https://static.wikitide.net/rosettacodewiki/d/db/Monte_Hall_problem.jpg", width=800)
st.title("Monty Hall Simulation")
counter = st.slider("Number of Simulations", min_value=100, max_value=10000, value=1000)
strategy = st.radio("Choose a strategy:", options=["Switch", "Stay"])


if strategy == "Switch":
    strategy = True

else:
    strategy = False


car, goat = counter_simulation(counter, strategy)
st.write(f"probability of winning a car: ```{car}```, probability of winning a goat: ```{goat}```")
