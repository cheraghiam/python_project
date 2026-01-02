import streamlit as st


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
        st.success("Profile user updated successfully!")
