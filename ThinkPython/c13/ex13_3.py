#!/usr/bin/env python3

arq=open('text.txt')

import string
s=string.punctuation
w=string.whitespace

print(w)

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
	inverse=dict()	
	d=dict()
	for item in lista:
		if item in d:
			d[item]+=1
		else:
			d[item]=1
	for item in d:
		inverse.setdefault(d[item], []).append(item)
	g=(sorted(inverse.items(), reverse=True))
	print(g[0:19])
	return g

count(arq)	
