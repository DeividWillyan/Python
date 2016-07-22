#!/usr/bin/python

# Deivid Willyan - V0.2 - 22/07/2016
# TeleBot, use => /exec ls
# Execulta comandos SO diretamente no telegram.
# Quaisquer duvidas - https://www.facebook.com/DeividWillyan
# Otimização de codigo, e estrica de documentação.


# import telegram api
import telegram, os
# import metodo sleep da biblioteca time 
from time import sleep

# cria o metodo main.
def main():

	# Variaveis necessarias para comunicação entre a API e telegram.
    update_id = None
    bot = telegram.Bot('TOKEN AQUI!!!!')
    print ('Bot Telegram iniciado...')
	
	# Loop Infinito
    while True:
        try:
			# A variavel update_id recebe o retoro do metodo botLHC.
            update_id = BotLHC(bot, update_id)
		# Caso seja encontrado uma falha de conexão, é retornada no servidor.
        except telegram.TelegramError as e:
            if e.message in ("Bad Gateway", "Timed out"):
                sleep(1)
			# caso seja encontrado outro erro generico, é apresentado no servidor o erro e logo em seguida
			# A API é encerrada.
            else:
                raise e
				print (e.message)
				exit(1)
        except URLError as e:
            sleep(1)

# Principal metodo utilizado na API, ela recebe dois paramentros
# o primeiro é o token criado pelo BotFather, o Segundo parametro é o comando a ser execultado.
def BotLHC(bot, update_id):
	# criaremos um loop que lé todas as atualizações (a cada 10 segundos) que o servidor recebe por parte do client (telegram)
	# a cada novo comando a variavel update recebe as informações do clint. (em forma de List.)
    for update in bot.getUpdates(offset = update_id, timeout = 10):
        # A variavel chat_id recebe a id de qual usuario fez a chamada ao sistema.
		chat_id = update.message.chat_id
		# A variavel update_id recebe a nova id, toda vez que é realizado uma nova chamada ao sistema.
        update_id = update.update_id + 1
		# a variavel message pega da lista retornada pra variavel update a key .message.text 
		# assim pegamos o que o usuario digitou no telegram de forma limpa.
        message = update.message.text
		
		# Criamos a variavel cmd que recebe o texto que foi enviado do nosso clint, ela é convertida 
		# para letras minusculas, e utilizamos o metodo split sem parametros, que por padrao utiliza 
	    # como default o espaço " ", para fatir a mensagem, depois deste processo, pegamos a primeira fatia
		# que foi disponibilizada pelo metodo split, [0].
		cmd = message.lower().split()[0]
		# A Variavel lenCmd recebe o tamanho real da palavra recortada.
        lenCmd = (len(cmd) + 1)
        
		# verificamos se nossa palavra recortada é igual ao padrao esperado.
		if(cmd == '/exec'):           
			# fazemos uma fatia manual da varial message, pegando apartir da segunda segunda posição
			# e pegamos o tamanho, verificamos se o mesmo é maior que zero, caso seja maior quer dizer que,
			# a um comando após o nosso padrao.
            if(len(message[lenCmd:]) > 0):
				# utilizamos agora o metodo sendMessage que é da API do telegram, este metodo envia para
				# o usuario que fez a requesição no inicio o retorno do comando execultado.
                bot.sendMessage(chat_id=chat_id, text='%s' % 
											# utilizamos o metodo popen, da bibliote os, que é referente
											# ao sistema operacional, este metodo execulta um comando e retorna]
											# o resultado no formato String.
											(os.popen('%s' % (message[lenCmd:])).read()))

        if(cmd == '/botQuit'):
            bot.sendMessage(chat_id, text='Finalizado com Sucesso!')
            sleep(5)            
			exit(1)
			
			

    return update_id



if __name__ == '__main__':
    main()
