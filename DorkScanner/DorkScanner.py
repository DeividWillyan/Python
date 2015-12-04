#!/usr/bin/env python3

import sys, urllib, urllib.request, simplejson

def DorkScanner(dork):
	queryDaBusca = urllib.parse.urlencode({'q' : dork})
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s&start=0' % (queryDaBusca)
	resultadosDaBusca = urllib.request.urlopen(url, None, None)
	json = simplejson.loads(resultadosDaBusca.read())
	results = json['responseData']['results']
	for i in results:
		y = i['url']
		x = y.replace("%3F", "?")
		z = x.replace("%3D", "=")
		print (z)

DorkScanner(dork = sys.argv[1])