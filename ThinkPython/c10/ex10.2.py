#!/usr/bin/env python3


def cumsum(t):
	total=0
	i=0
	lista=[]
	for item in t:
		total=total+t[i]
		lista.append(total)
		i=i+1
	print(lista)
	return lista
	

a=[1,2,3,4,5,6]
cumsum(a)

