import urllib

thisurl = raw_input("Entre com o site: ")
handle = urllib.urlopen(thisurl)
html_gunk =  handle.read()
print html_gunk