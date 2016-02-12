#!/usr/bin/python3
# Deivid Willyan
# TwitterAPI, pega 5 tweets.
# V0.1 - 12/02/2016

import codecs
import sys
from TwitterAPI import TwitterAPI

#sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

# TwitterAPI KEY DEVELOPER
################################################################################### 

consumer_key = 'KEY AQUI'
consumer_secret = 'KEY SECRET AQUI'
access_token = 'TOKEN AQUI'
access_secret = 'TOKEN SECRET AQUI'

####################################################################################

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)

pes = input('Pesquisa: ')
print()

i = 1
for item in api.request('search/tweets', {'q': pes, 'count': 5}):
    print('[', i, '] ' , item['text'] if 'text' in item else item)
    i= i+1

print()         
