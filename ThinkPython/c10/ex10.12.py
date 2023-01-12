#!/usr/bin/env python3

import bisect

arq=open('words.txt')

from ex1010 import arq_lista 

t=arq_lista(arq)


def inlist(b, f):
	for item in b:
		if item == f:
			return True	
#			return bisect.bisect(b, f)
	return False

def pair(t,word):
	even=word[::2]
	odd=word[1::2]
	return inlist(t, even) and inlist(t, odd)

for word in t:
	if pair(t, word):
		print(word, word[::2], word[1::2])
