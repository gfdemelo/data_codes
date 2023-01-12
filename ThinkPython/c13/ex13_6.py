#!/usr/bin/env python3

arq=open('text.txt')
arq2=open('words.txt')

import string
s=string.punctuation
w=string.whitespace


def arq_dic(t):
	d=dict()
	for line in t:
		a=line.strip().lower()
		d[a]=True
	return d


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
	return d
arquivo=arq_dic(arq2)

#for item in count(arq):
#	if item not in arquivo:
#		print(item)

def subtract(d1, d2):
	return set(d2)-set(d1)


print(subtract(arquivo, count(arq)))	
