#!/usr/bin/env python



def fatorial(n):
	return 1 if n == 0 else n*fatorial(n-1)

def divisible(n):
	a=fatorial(n)
	lista=list(str(a))
#	print(a)
#	print(lista)
	lista2=[]
	for i in range(len(lista)):
		lista2.append(int(lista[i]))
#	print(sum(lista2))
	if a % sum(lista2) ==0:
		return True
	return False
		
		
if __name__=='__main__':
	for i in range(500):
		if not divisible(i):
			print(i,'   -    ', divisible(i))
	
	
	
