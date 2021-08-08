import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# mensagem
msg = MIMEMultipart()
message = "Email recebido!"

# Cred. e assuntos #
password = "*** Senha do seu e-mail ***"
msg['From'] = "*** login do e-mail que vai enviar  ***"
msg['To'] = "*** login do e-mail que vai receber ***"
msg['Subject'] = "Enviando gmail " # Assunto

# conexão e envia o email #
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()