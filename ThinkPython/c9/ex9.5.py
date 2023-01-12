#!/usr/bin/env python3

arq=open('words.txt')
letras=input('Digite uma sequência de letras a serem usadas: ')


def avoids(word, letras):
	for alfa in letras:
			if alfa not in word:
				return False
	return True

def uses_all(t, letras):
	count=0
	for line in t:
		a=line.strip()
		if avoids(a, letras):
			count=count+1
			print(a)
	print(count)


uses_all(arq, letras)	
