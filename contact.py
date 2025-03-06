import smtplib as sm
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(message):
    host="smtp.gmail.com"
    port=465

    username="harisharish982005@gmail.com"
    password="hjrylrlhcppvashw"

    reciver="harisharish982005@gmail.com"
    with sm.SMTP_SSL(host,port) as sever:
        sever.login(username,password)
        sever.sendmail(username,reciver,message)
