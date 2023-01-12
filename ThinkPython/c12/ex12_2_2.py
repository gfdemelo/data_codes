#!/usr/bin/env python3

arq=open('words.txt')


def invert_dict(d):
	inverse=dict()
	for key in d:
		inverse.setdefault(tuple(d[key]), []).append(key)	
	return inverse


def arq_lista(t):
	lista=[]
	for line in t:
		lista.append(line.strip())
	return lista

def lista_dicio(a):
	d={}
	t=arq_lista(a)
	for word in t:
		l=[]
		for char in word:
			l.append(char)
			l.sort()
		d.setdefault(word, l)#.append(char)				
	return d

def anagrama(t):
	a=lista_dicio(arq)
	b=invert_dict(a)
	lista=[]
	for val in b.values():
		if len(val)>1:
			lista.append(val)
	return	sorted(lista, key=len)#, reverse=True)
		
	
print(anagrama(arq))
#print(lista_dicio(arq))			
