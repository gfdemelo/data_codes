#!/usr/bin/env python3

import bisect

arq=open('words.txt')
#word=input('Palavra a ser procurada: ')

def arq_lista(t):
	lista=[]
	for line in t:
		a=line.strip()
		lista.append(a)
	return lista



def inlist(a, f):
	b=arq_lista(a)
	for item in b:
		if item == word:
			return bisect.bisect(b, f)
	return None


#print(inlist(arq, word))	

