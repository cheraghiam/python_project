import yagmail


yag = yagmail.SMTP('your email address', 'your gmail app password')
contents = ['This is the body, and here is just text']
yag.send('pythonicpage@gmail.com', 'subject', contents)

if __name__ == "__main__":
    print("Email sent successfully!")