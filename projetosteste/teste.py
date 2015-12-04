import urllib, urllib.request

def leituraWordlist():	

	wordlist_file = "/pentest/wordlist/diretorios/all.txt"	
	alvo = "http://www.unifil.br"

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

leituraWordlist()