#!/usr/bin/env python3

arq=open('portugues.txt')
alpha=('a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def text_str(t):
	lista=[]
	for word in t:
		lista.append(word.split()) 
	return lista

#text_str(arq)

def invert_dict(d):
	inverse=dict()
	for key in d:
		inverse.setdefault(d[key], []).append(key)	
	return inverse


def most_frequent(t):
	i=0
	d={}
	for word in t:
		for char in word.lower():
			if char in alpha:
				if char in d:
					d[char]=d[char]+1
				else:
					d[char]=i+1
	soma=sum(d.values())
	dicionario=invert_dict(d)
	for value, key in sorted(dicionario.items(), reverse=True):
		print(key,'-', (value/soma)*100, '%')



most_frequent(arq)
		
			


	
