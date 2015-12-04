#!/usr/bin/env python3

import sys, urllib, urllib.request

def crawler(crawlerscan, wordlist):	

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

crawler(crawlerscan = sys.argv[1], wordlist = sys.argv[2])