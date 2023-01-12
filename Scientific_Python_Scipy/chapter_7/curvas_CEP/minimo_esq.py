#!/usr/bin/env python3


arq=open('esq')




def minimo(t):
	lista=[]
	d=dict()
	for line in t:
		a=line.strip().split()
		lista.append((a))
	for item in lista:
		for index in item:
			a=str_2_flt(index)
			d[a]=True
	print(min(d))
			
		
def str_2_flt(t):
	return float(t)
		
minimo(arq)	
