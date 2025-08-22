import streamlit as st
from src.main import RockPaperScissors


rps_image_url = (
	'https://static.vecteezy.com/system/resources/previews/012/616/132/non_2x/'
	'rock-paper-scissors-icon-set-on-white-background-vector.jpg'
)
st.image(rps_image_url)
name = st.text_input('Enter Your Name: ')
rps = RockPaperScissors(name=name)
st.write(f'Hi {name}, welcome to the game!')
user_choice = st.radio(
	"Choose your move:", options=['Rock', 'Paper', 'Scissors']
)
item_computer = rps.get_item_from_computer()
item_user = rps.get_item_from_user(user_choice=user_choice)
result = rps.check_result(item_computer=item_computer, item_user=item_user)
st.write(f'Computer chose: {item_computer}, You chose: {item_user}')
st.write(result)
