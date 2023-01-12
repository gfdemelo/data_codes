#!/usr/bin/env python3

arq=open('words.txt')
letras=input('Digite uma sequência de letras proibidas: ')


def avoids(word, letras):
	for char in word:
		for alfa in letras:
			if alfa  == char:
				return False
	return True

def avoid(t, letras):
	count=113810
	for line in t:
		a=line.strip()
		if not avoids(a, letras):
			count=count-1
	print(count)

avoid(arq, letras)	
