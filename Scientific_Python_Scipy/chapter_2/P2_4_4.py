#!/usr/bin/env python


import math
known={0:1}

#def fatorial(t):
#	return 1 if t==0 else fatorial(t-1)*t


def pascal(n, p):
	if p in known:
		return known[p]
	elif n==p:
		return 1
	else:
		return int(math.factorial(n)/(math.factorial(p)*(math.factorial(n-p))))


if __name__=='__main__':
	for i in range(8):
		print('Linha %.d -' % (i), end=' ')
		for j in range(i+1):
			print(pascal(i,j), end=' ')
		print('\n')
					
