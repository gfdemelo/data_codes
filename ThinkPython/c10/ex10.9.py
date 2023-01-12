#!/usr/bin/env python3



arq=open('words.txt')



def lista(t):
	s=[]
	for line in t:
		a=line.strip()
		s.append(a)
	return s

def lista2(t):
	s=[]
	for line in t:
		a=line.strip()
		s=s+[a]
	return s



print(lista(arq))


	
