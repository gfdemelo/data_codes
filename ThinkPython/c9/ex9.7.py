#!/usr/bin/env python3


#user=input('Digite uma palavra com três duplas consecutivas: ')


def silabas_duplas(t):
	i=0
	c=0
	while i+5 < len(t)-1:
		if t[i]==t[i+1] and t[i+2]==t[i+3] and t[i+4]==t[i+5]:
#			print('True')
			return True
		else:
			i=i+1
#	print('False')
	return(False)


def find_file():
	arq=open('words.txt')
	for line in arq:
		a=line.strip()
		if silabas_duplas(a):
			print(a)



find_file()			

