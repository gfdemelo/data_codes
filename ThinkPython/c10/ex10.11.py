#!/usr/bin/env python3

import bisect

arq=open('words.txt')

def arq_lista(t):
	lista=[]
	for line in t:
		a=line.strip()
		lista.append(a)
	return lista

def reverse_pair(f, a):
	c=a[::-1]
	h=bisect.bisect_left(f, c)
	if h<len(f):
		if f[h]==c:
			return True
	else:
		return False
def reverso(t):
	f=arq_lista(t)
	for line in f:
		if reverse_pair(f, line):
			print(line, '- ', line[::-1])


reverso(arq)
