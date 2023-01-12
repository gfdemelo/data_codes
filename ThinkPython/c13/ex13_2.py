#!/usr/bin/env python3

arq=open('text.txt')

import string
s=string.punctuation
w=string.whitespace


def string(t):	
	lista=[]
	for line in t:
		for word in line.split():
			word=word.replace('-', '')
			word=word.replace('"', '')
			word=word.replace('.', '')
			word=word.strip(s+w).lower()
			lista.append(word)
	return lista



def count(t):
	lista=string(t)
	
	d=dict()
	for item in lista:
		if item in d:
			d[item]+=1
		else:
			d[item]=1
	for item in d:
		print(item, '-', d[item])
	print('O número de palavras diferentes no livro é ', len(d))	
	print('O número total de palavras no livro é: ', len(lista))
	#return d

print(count(arq))
