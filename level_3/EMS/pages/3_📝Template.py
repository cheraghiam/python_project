import streamlit as st


st.title("Email Templates")

with st.form("email_template_form"):
    template_name = st.text_input("Template Name")
    subject = st.text_input("Email Subject")
    body = st.text_area("Email Body", height=400)

    submitted = st.form_submit_button("Save Template")

    if submitted:
        st.success("Email template saved successfully!")