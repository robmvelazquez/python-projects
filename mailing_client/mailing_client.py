import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = #insert sender email here.
email_password = #insert password here.
email_receiver = #insert recipient email here.

subject = "Automated Email"
body = """
Automated Email test successful!
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
