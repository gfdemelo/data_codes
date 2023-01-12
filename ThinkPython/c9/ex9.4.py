#!/usr/bin/env python3

arq=open('words.txt')
letras=input('Digite uma sequência de letras a serem usadas: ')


def avoids(word, letras):
	for char in word:
			if char not in letras:
				return False
	return True

def uses_only(t, letras):
	count=0
	for line in t:
		a=line.strip()
		if avoids(a, letras):
			count=count+1
			print(a)
	print(count)


uses_only(arq, letras)	
