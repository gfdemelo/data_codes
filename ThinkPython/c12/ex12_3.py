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
#	print(b)
	lista=[]
	for val in b.values():
		if len(val)>1:
			lista.append(val)
	return lista
		
def metatese(t):
	x=anagrama(t)
	i=0
	j=i+1
	for item in x:
		for i in range(len(item)-1):
			for j in range(len(item)):
				lista=list()
				a=zip(item[i], item[j])	
				for pair,par in a:
					if pair!= par:
						a=[pair, par]
						lista.append(a)
				if len(lista)==2:
					print(item[i], '- ', item[j])
#				j+=1
#			i+=1
metatese(arq)
#print(lista_dicio(arq))	
#anagrama(arq)
#print(lista_dicio(arq))		













	
