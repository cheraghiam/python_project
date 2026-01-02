import streamlit as st


st.title("👤 User Profile")

col1, col2 = st.columns(2)

with st.form("user_profile_form"):
    with col1:
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
    with col2:
        email = st.text_input("Email Address")
        degree = st.text_input("Degree")

    submitted = st.form_submit_button("Update Profile")

    if submitted:
        st.success("Profile updated successfully!")
