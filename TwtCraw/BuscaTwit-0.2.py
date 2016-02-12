#!/usr/bin/python3
# Deivid Willyan
# TwitterAPI, pega 5 tweets.
# V0.1 - 12/02/2016
# OrganizaÃ§Ã£o de Codigo e Melhoridas Gerais.
# V0.2 - 12/02/2016
# pip install TwitterAPI

from TwitterAPI import TwitterAPI

consumer_key = 'KEY AQUI'
consumer_secret = 'KEY SECRET AQUI'
access_token = 'TOKEN AQUI'
access_secret = 'TOKEN SECRET AQUI'

def busca(pesq):
    api = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)
    req = api.request('search/tweets', {'q': pesq, 'count': 5, 'lang' : 'pt'})

    i = 1
    for item in req:
        if 'text' in item:
            print('[', i, '] ' , item['text'])
            i += 1
        else:
            item

def main():
    pesq = input('Pesquisa: ')
    busca(pesq)

if __name__ == '__main__':
    main()

 
