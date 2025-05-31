import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "smaran.vidhya@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "smaran.vidhya@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user=username, password=password)
        server.sendmail(username, receiver, message)