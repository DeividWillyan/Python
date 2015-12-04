import urllib, simplejson
"""from pygoogle import pygoogle


def exemplo1():
	g = pygoogle('deivid')
	g.pages = 1
	print ('Encontrado %s resultados' %(g.get_result_count())	

	for i in g.get_urls():
		print (i) """





def Search_Function(query, number):
    query = urllib.urlencode({'q':query})
    index = number//4
    if index%4!=0:index += 1 #To get more results than what user asked so that we dont fall short
    for i in xrange(0,index):
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&start='+str(index*4)+'&'+query
        search_results = urllib.urlopen(url)
        json = simplejson.loads(search_results.read())
        results = json['responseData']['results']
        for item in results:
            if number == 0:
                break
            print (item['title'] + ": " + item['url'])
            number -= 1

if __name__ == "__main__":
    query = raw_input('Please enter the query: ')
    number = int(raw_input('Please enter the number of results: '))
    Search_Function(query, number)