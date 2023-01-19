import email, smtplib, ssl

from email import encoders
from email.mine.base import MINEBase
from email.mine.multipart import Mi



port = 465

PASSWORD = ''
email = 'peerezjoao1@gmail.com'

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(email, password)