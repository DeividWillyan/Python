#!/usr/bin/python3
# Autor: Deivid Willyan
# Email: deiviid_@hotmail.com
# Versao: V0.1 - 12/02/2016
# pip install TwitterAPI

# -*- coding: ascii -*-

from TwitterAPI import TwitterAPI

consumer_key = 'KEY AQUI'
consumer_secret = 'KEY SECRET AQUI'
access_token = 'TOKEN AQUI'
access_secret = 'TOKEN SECRET AQUI'


api = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)

TWEET_TEXT = "Deivid Testing Python API3"
r = api.request('statuses/update', {'status': TWEET_TEXT})
print('SUCCESS' if r.status_code == 200 else 'FAILURE')
