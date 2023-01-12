#!/usr/bin/env python

def normalize(t):
	lista=list()
	for item in t:
		lista.append((item-min(t))/(max(t)-min(t)))
	return lista

a=[2,4,10,6,8,4]
print(normalize(a))
		
