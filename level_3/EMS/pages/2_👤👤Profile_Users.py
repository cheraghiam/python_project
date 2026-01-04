import streamlit as st
from EMS.db import profile_user_table


st.title("Profile Users")

col1, col2 = st.columns(2)

with st.form("profile_users_form"):
    with col1:
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
    with col2:
        email = st.text_input("Email Address")
        profession = st.text_input("Profession")

    submitted = st.form_submit_button("Update User")

    if submitted:
        profile_user_table.insert({
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'profession' : profession
        })

        st.success("Profile user updated successfully!")
