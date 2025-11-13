import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("warzone84@gmail.com", "vhrr mvol oufn fztu")
message = "Message_you_need_to_send"
s.sendmail("warzone8419@gmail.com", "warzone8419@gmail.com", message)
s.quit()
