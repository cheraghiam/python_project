import streamlit as st 


st.title("📧 Send Email")

with st.form("send_email_form"):
    recipient = st.text_input("Recipient Email Address")
    subject = st.text_input("Email Subject")
    message = st.text_area("Email Message", height=300)
    submitted = st.form_submit_button("Send Email")

    if submitted:
        # Here you would add the logic to send the email
        st.success(f"Email sent to {recipient} successfully!")