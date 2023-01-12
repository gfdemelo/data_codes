#!/usr/bin/env python3

import string, random, bisect

arq=open('text.txt')

s=string.punctuation
w=string.whitespace

def book_list(t):
	lista=[]
	for line in t:
		for word in line.split():
			word=word.replace('-', ' ')
			word=word.strip(s+w).lower()
			lista.append(word)
	return lista


def soma_cumulativa(t):
	lista=[]
	i=0
	for item in t:
		i+=1	
		lista.append(i)
	return lista


def find_word(t):
	a=soma_cumulativa(t)
	n=random.randint(1, a[-1])
	f=bisect.bisect(a, n)
	return t[f]

b=book_list(arq)		
for i in range(1,50):
	print(find_word(b))		
