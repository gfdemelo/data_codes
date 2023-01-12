#!/usr/bin/env python3

dicionario=dict()

def has_duplicates(l):
	for item in l:
		if item in dicionario:
			return True 
		dicionario[item]=0
	return False


x=[1,2,5,4,5,6,7]
print(has_duplicates(x))
