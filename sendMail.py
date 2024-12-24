import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
sender_email = os.getenv('SENDER_EMAIL')
sender_passwoord = os.getenv('SENDER_PASSWORD')
recipient_email = os.getenv('RECIEVER_EMAIL')

def send_email(text, subject):
    smtp_server = 'smtp.gmail.com'
    port = 587

    message = MIMEText(text)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
 
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_passwoord)
        server.sendmail(sender_email, recipient_email, message.as_string())
    
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, sender_passwoord)
            server.sendmail(sender_email, recipient_email, message.as_string())
    except smtplib.SMTPAuthenticationError:
        print('Hata: Kimlik doğrulama başarısız oldu.')