import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()


server.login("robmvelazquez@gmail.com", "Talissav2013")

msg = MIMEMultipart()
msg["From"] = "RobV"
msg["To"] = "rmejia011@yahoo.com"
msg["Subject"] = "Just a test."

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

filename = ""
attachment = open(filename, "rb")

p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f' attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail("robmvelazquez@gmail.com", "rmejia011@yahoo.com", text)