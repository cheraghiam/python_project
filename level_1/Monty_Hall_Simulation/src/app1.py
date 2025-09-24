import streamlit as st


st.markdown("## Monty Hall Simulation")

selected_door = st.selectbox("Choose a door", options=["Door 1", "Door 2", "Door 3"])
st.write(f"You selected: {selected_door}")
st.write(f"door '' is goat")

switch = st.radio("Do You Wont Switch your door?", options=["Yes", "NO"])