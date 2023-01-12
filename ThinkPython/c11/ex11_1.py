#!/usr/bin/env python3

arq=open('words.txt')


def dicionario(t):
	word=dict()
	i=0
	for line in t:
		a=line.strip()
		word[a]=i
		i+=1
	print(word)	

dicionario(arq)
		
		
