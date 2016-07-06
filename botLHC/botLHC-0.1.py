#!/usr/bin/python

# Deivid Willyan - V0.1 - 06/07/2016
# TeleBot, use => /exec ls
# Execulta comandos SO diretamente no telegram.
# Quaisquer duvidas - https://www.facebook.com/DeividWillyan

import telegram, os
from time import sleep

def main():

    update_id = None
    bot = telegram.Bot('TOKEN AQUI!!!!')
    print ('Bot Telegram iniciado...')

    while True:
        try:
            update_id = BotLHC(bot, update_id)
        except telegram.TelegramError as e:
            if e.message in ("Bad Gateway", "Timed out"):
                sleep(1)
            else:
                raise e
        except URLError as e:
            sleep(1)

def BotLHC(bot, update_id):
    for update in bot.getUpdates(offset=update_id, timeout=2):
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        message = update.message.text

        if(message.lower().split()[0] == "/exec"):
           if(len(message[6:]) > 0):
                bot.sendMessage(chat_id=chat_id, text="%s" % (os.popen('%s' % (message[6:])).read()) )


    return update_id



if __name__ == '__main__':
    main()
