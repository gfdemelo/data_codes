#!/usr/bin/env python3

arq=open('text.txt')

import string, math

s=string.punctuation
w=string.whitespace

def string(t):
	lista=[]
	for line in t:
		for word in line.split():
			word=word.replace('-', '')
			word=word.strip(s+w)
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
	g=(sorted(inverse.keys(), reverse=True))
	print(g[:10])
	print('log f', '\t', 'log r')
	for i in range(len(g)):	
		print(math.log(g[i],10),'\t',  math.log(i+1,10))
	return d

count(arq)
