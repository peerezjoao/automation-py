import os
import pathlib
from dotenv import load_dotenv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

# dados do remetente
remetente  = os.getenv('FROM_EMAIL')
destinatario = os.getenv('FROM_EMAIL')

# Configuracoes do SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD')

# mensagem de texto
with open(CAMINHO_HTML, 'r') as corpo_email:
    texto_arquivo = corpo_email.read()
    template = Template(texto_arquivo)
    #texto_email = template.substitute()

# transformar corpo em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] =  destinatario
mime_multipart['subject'] = 'Raspagem de dados.'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)
 

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso.')