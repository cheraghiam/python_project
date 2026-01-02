import streamlit as st
from datetime import date, time


st.title("📅 Schedule Email")

send_date = st.date_input("Select Date", value=None)
send_time = st.time_input("Select Time", value=None)

if st.button("Save Schedule"):
    st.success(f"Email scheduled for {send_date} at {send_time}!")