#!/usr/bin/env python3

dicionario={}
lista=['cheer', 'jolly', 'cheer','melon', 'cubed']
arq=open('words.txt')



from ex8_5 import rotate_word


def arq_lista(t):
	lista=[]
	for word in t:
		a=word.strip()
		lista.append(a)
	return lista	


def rotation(l, r):
	i=1
	for word in l:
		dicionario[word]=None
		for i in range (1,r):
			a=rotate_word(word, i)
			if a in dicionario:
				print(word, i, a)

rotation(arq_lista(arq), 3)
#rotate_word(lista[0], 7)

