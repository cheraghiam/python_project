import streamlit as st

from src.game_logic import find_another_goat
from src.game_logic import result


st.markdown("## Monty Hall Simulation")

selected_door = st.selectbox("Choose a door", options=[1, 2, 3])

another_gaot = find_another_goat(user_input=selected_door - 1)

st.write(f"You selected: {selected_door}")
st.write(f"door {another_gaot}' is goat")

switch = st.radio("Do You Wont Switch your door?", options=["Yes", "NO"])

if switch == "Yes":
    switch == True
else:
    switch == False

show_result = result(user_input=selected_door, another_goat=another_gaot, switch=switch)

st.write(show_result)
