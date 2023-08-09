import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Mat"
email["to"] = "foxherrera01@gmail.com"
email["subject"] = "YOU WON 1,000,000 DOLLARS!"


email.set_content(html.substitute({"name": "TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mattherr23@gmail.com", "wziwmjrotxehsmix")
    smtp.send_message(email)
    print("all done!")
