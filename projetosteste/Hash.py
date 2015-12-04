import hashlib
import sys

def md5(entrada):
	conversao = hashlib.md5(entrada.encode())
	print(conversao.hexdigest())

def sha1(entrada):
	conversao = hashlib.sha1(entrada.encode())
	print(conversao.hexdigest())



escolha = raw_input("md5 ou sha1: ")
if escolha == "md5":
	entrada = raw_input("Entre com a String: ")
	md5(entrada)
elif escolha == "sha1":
	entrada = raw_input("Entre com a String: ")
	sha1(entrada)
