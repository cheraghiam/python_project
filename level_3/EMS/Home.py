import streamlit as st

st.set_page_config(
    page_title="Email Management System",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Email Management Dashboard")

st.markdown("""
### Welcome 👋  
Use this system to manage users, email templates, scheduling, and sending emails.

#### Features:
- 👤 User Profile
- 👥 Profile Users
- 📝 Email Templates
- ⏰ Email Scheduling
- 📤 Send Email
""")

st.info("Select a page from the sidebar to get started.")
