#!/usr/bin/env python3

import random


arq=int(input('Número de amostras: '))
arc=int(input('Número de simulações: '))


def birthday(a):
	lista=[]
	for i in range(a):	
		t=random.randint(1,365)
		lista.append(t)
	return lista	

def duplicado(b):
	i=0
	c=sorted(b)
	for i in range(len(c)-1):
		if c[i] == c[i+1]:
			return True
	return False


def simulation(q, r):
	count=0
	for i in range(q):
		t=birthday(r)		
		if duplicado(t):
			count += 1
	return count


def main():
	print('Após %d simulações' % arc)
	print('com %s estudantes' % arq)
	print('foram', simulation(arc, arq),'simulações com ao menos um aniversário igual')

if __name__ == '__main__':
	main()
		

				
