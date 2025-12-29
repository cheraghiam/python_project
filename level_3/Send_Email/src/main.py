import smtplib
from email.mime.text import MIMEText


msg = MIMEText('Hello, this is a test email')
msg['Subject'] = 'Test email'
msg['From'] = 'your gmail address'
msg['To'] = 'recipient email address'

server = smtplib.SMTP('smtp.gmail.com', 587)
sender_email = 'your gmail address'
password = 'your gmail app password'

server.starttls()
server.login(sender_email, password)
server.send_message(msg)
server.quit()
print("Email sent successfully!")
