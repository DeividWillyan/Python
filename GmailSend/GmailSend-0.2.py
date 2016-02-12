#!/usr/bin/python3
# Deivid Willyan
# Envio de Emails Com Python!
# V0.2 - 12/02/2016
# Melhoria no Codigo.
# Adicionado threading

# INFO :  https://www.google.com/settings/security/lesssecureapps  > Permitir Dispositivos Menos Seguros "Ativar"

import smtplib
from threading import Thread

def envio(dst):
    usr = 'email@gmail.com'
    pwd = 'senha'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(usr, pwd)

    msg = 'Mensagem De Teste Python'
    assunto = 'Assunto Python'
    format = 'Subject: %s\n\n%s' % (assunto, msg)

    server.sendmail(usr, dst, format)
    server.quit()

def main():
    dst = input('Destinatario: ')
    for env in range(10):
        t = Thread(target=envio, args=(dst,))
        t.start()
    print('Envio Concluido!')

if __name__ == '__main__':
    main()
