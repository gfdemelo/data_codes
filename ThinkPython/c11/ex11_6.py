#!/usr/bin/env python3


arq=open('words.txt')

from pronounce import read_dictionary


def arq_lista(t):
	lista=[]
	for item in t:
		a=item.strip()
		lista.append(a)
	return lista

def homofono():
	#a=read_dictionary()
	#for item in arq_lista(l):
	item.upper()
	c=item[1:]
	d=item[0]+item[2:]
	if item in a and c in a and d in a:
		if a[item]==a[c] and a[item]==a[d]:
			return True	
		


if __name__ == '__main__':		
	arquivo=arq_lista(arq)
	a=read_dictionary()
	for item in arquivo:
		if homofono():
			print(item, item[1:], item[0]+item[2:])		
