#!/usr/bin/env python3

import os

#molecula=input('Digite a molecula: ')
#estados=input('Digite o número de estados: ')


def find(filename, distancia, estados):
	a=open('esq', 'w')
	d=dict()
	lista=[]
	for line in open(filename):
		if line.startswith(' SETTING '+'R'+distancia):
			b=line.split(' ')			
			a.write(b[20])
		if line.startswith(' SETTING '+distancia):	
			c=line.split(' ')
			a.write('	'+c[16])
			lista.append(c[16])
		if len(lista)==(estados):
			d[b[20]]=lista
			a.write('\n')
			lista=[]
	
	a.close()


find('SI+.out', 'SI', 25)
