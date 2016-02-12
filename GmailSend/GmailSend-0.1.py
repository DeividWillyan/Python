#!/usr/bin/python3
# Deivid Willyan
# Envio de Emails Com Python!
# V0.1 - 12/02/2016

import smtplib

usr = 'email@gmail.com'
pwd = 'senha'
dst = input('Destinatario: ')

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(usr, pwd)

server.sendmail(usr, dst, 'Python Rocks!')

server.quit()
