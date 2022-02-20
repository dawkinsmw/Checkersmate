import smtplib
import os

def send_email(subject, body, sender = 'dawkinsmw.dev@gmail.com', reciever = 'mark.dawkins94@gmail.com'):
    msg = f"Subject: {subject}\n\n{body}"
    pw = os.getenv('EMAIL_PW')

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, pw)
        smtp.sendmail(sender, reciever, msg)
