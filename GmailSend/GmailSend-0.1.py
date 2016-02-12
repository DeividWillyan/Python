#!/usr/bin/python3
# Deivid Willyan
# Envio de Emails Com Python!
# V0.1 - 12/02/2016

import smtplib

usr = 'deividwillyan.email@gmail.com'
pwd = 'python123'
dst = input('Destinatario: ')

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(usr, pwd)

asnt = 'Deivid'

server.sendmail(usr, dst, 'Python Rocks!')

server.quit()
