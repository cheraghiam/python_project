import streamlit as st
from EMS.db import schedule_table   


st.title("Schedule Email")

send_date = st.date_input("Select Date", value=None)
send_time = st.time_input("Select Time", value=None)

if st.button("Save Schedule"):
    schedule_table.insert({
        'send_date' : str(send_date),
        'send_time' : str(send_time)
    })

    st.success(f"Email scheduled for {send_date} at {send_time}!")