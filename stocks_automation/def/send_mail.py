import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_addr = 'echobotuipath@gmail.com'
to_addr = 'peerezjoao1@gmail.com'
subject = 'Relatório Gerencial disponível para download: '
content = 'Segue o relatório gerencial do fundo:'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

filename = "C:\Users\peere\Downloads\DAS-PGMEI-44395425000112-AC2022 (1).pdf"
with open(filename, 'r') as f:
    attachment = MIMEApplication(f.read(), Name=basename(filename))
    attachment['Content-Disposition'] - 'attachment; filename-"{}'.format(basename(filename))
    
    
msg.attach(attachment)

server = smtplib.SMTP('smtp.dreamhost.com',587)
server.login(from_addr, 'mystrongpw!')