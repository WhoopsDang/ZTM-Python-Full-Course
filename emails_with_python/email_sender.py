import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Mat"
email["to"] = "foxherrera01@gmail.com"
email["subject"] = "YOU WON 1,000,000 DOLLARS!"


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mattherr23@gmail.com", "wziwmjrotxehsmix")
    smtp.send_message(email)
    print("all done!")
