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
			print(word)
#			for char in word:
#				if char in s:
#					f=word.replace(char, '')
#					lista.append(word)

#	for item in lista:
#		print(item)
		

string(arq)
