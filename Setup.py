import os
import smtplib
from email.message import EmailMessage
import webbrowser

def send_email(subject, body, attachment_file):
    gmail_user = " "
    gmail_password = " "

    msg = EmailMessage()
    msg.set_content(body)

    if os.path.isfile(attachment_file):
        with open(attachment_file, 'rb') as f:
            msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=attachment_file)
    else:
        print(f"Error: The file '{attachment_file}' does not exist.")
        return  # Exit the function if the file is not found

    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = 'support@telegram.org'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(msg)

def create_gmail_and_send_email():
    while True:
        username = input("Enter a new Gmail username: ")
        password = input("Enter a new Gmail password: ")

        send_email("Check this", "Here's the file for you", "AUTHS.txt")

        webbrowser.open(f"https://mail.google.com/mail/u/0/#inbox?compose=new")

if __name__ == "__main__":
    create_gmail_and_send_email()
