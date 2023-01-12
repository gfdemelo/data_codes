#!/usr/bin/env python

import copy

def inteiros(t):
	lista=[]
	for i in range(len(t)):
		l=copy.copy(t)
		l.pop(i)
		a=1
		for j in range(len(l)):
			a*=l[j]
		lista.append(a)
	print(lista)

x=[1,2,3]
inteiros(x)

