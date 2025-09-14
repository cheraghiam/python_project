import requests
import streamlit as st
from src.main import exchange_rates


url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
Currency = list(response.json()['rates'].keys())

st.markdown("# :dollar: Currency Converter")
st.markdown("""
This app converts an amount from one currency to another using real-time exchange rates.
""")

col1, col2 = st.columns(2)
base_select_box = col1.selectbox('Base Currency', Currency)
target_select_bos = col2.selectbox('Target Currency', Currency)

basecr, targetcr = exchange_rates(base_select_box, target_select_bos)

st.markdown(f'### 1 {base_select_box} = {targetcr/basecr:.4f} {target_select_bos}')

