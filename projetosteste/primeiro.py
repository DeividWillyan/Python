#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random

numero = random.randint(1,100)

tentativas = 0
escolha = 0

while escolha != numero:
	escolha = input("Informa um numero até 100: ")
	tentativas += 1
	if escolha > numero:
		print "Maior"
	elif escolha < numero:
		print "Menor"

print "\nAcertou, O numero sorteado era", numero
print "Voce usou", tentativas, "tentativas"