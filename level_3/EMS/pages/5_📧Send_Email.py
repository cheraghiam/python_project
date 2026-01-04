import streamlit as st
import yagmail
import json
from datetime import datetime

# -------------------------------
# Load database
# -------------------------------
with open("db.json") as f:
    db = json.load(f)

users = db["users"]
templates = db["templates"]
profiles = db["profile_users"]
schedules = db["schedules"]

st.title("📧 Email Sender Panel")

# -------------------------------
# Select recipients (profile_users)
# -------------------------------
profile_options = {
    f"{p['first_name']} {p['last_name']} ({p['email']})": p["email"]
    for p in profiles.values()
}

selected_profiles = st.multiselect(
    "Select Recipients",
    options=list(profile_options.keys())
)

recipients = [profile_options[p] for p in selected_profiles]

# -------------------------------
# Select template
# -------------------------------
template_options = {
    t["template_name"]: t
    for t in templates.values()
}

template_name = st.selectbox(
    "Select Email Template",
    list(template_options.keys())
)

template = template_options[template_name]

# -------------------------------
# Email content
# -------------------------------
subject = st.text_input("Subject", value=template["subject"])
body = st.text_area("Body", value=template["body"], height=300)

# -------------------------------
# Schedule checkbox
# -------------------------------
schedule_enabled = st.checkbox("⏰ Schedule Email")

if schedule_enabled:
    schedule_options = {
        f"{s['send_date']} {s['send_time']}": s
        for s in schedules.values()
    }

    selected_schedule = st.selectbox(
        "Select Schedule Time",
        list(schedule_options.keys())
    )

    schedule_data = schedule_options[selected_schedule]
    send_at = datetime.fromisoformat(
        f"{schedule_data['send_date']} {schedule_data['send_time']}"
    )

st.divider()

# -------------------------------
# Actions
# -------------------------------
col1, col2 = st.columns(2)

def send_now():
    yag = yagmail.SMTP(
        'your_email@gmail.com',
        "your app_passwords"
    )
    for email in recipients:
        yag.send(email, subject, [body])

# 🔹 Send Now
if col1.button("🚀 Send Now"):
    if not recipients:
        st.error("❌ Please select recipients")
    else:
        send_now()
        st.success("✅ Email sent successfully")

# 🔹 Schedule
if col2.button("💾 Save Schedule"):
    if not schedule_enabled:
        st.warning("⚠️ Schedule is not enabled")
    elif send_at <= datetime.now():
        st.error("❌ Scheduled time must be in the future")
    else:
        scheduled_email = {
            "recipients": recipients,
            "subject": subject,
            "body": body,
            "send_at": send_at.isoformat(),
            "status": "pending"
        }

        db.setdefault("scheduled_emails", []).append(scheduled_email)

        with open("db.json", "w") as f:
            json.dump(db, f, indent=4)

        st.success("🕒 Email scheduled successfully")
