#!/usr/bin/env python

import math

def madhava(n):
	pi=math.sqrt(12)
	a=0
	j=0
	for i in range(1,n,2):
		if i ==1:
			a+=1
		elif j %2 != 0:
			a-= 1/(i*3**j)
		else: 
			a+= 1/(i*3**j)
		j+=1
	print('pi = ', a*pi)

madhava(20)
			
def madhava_livro(n):
	""" Resolução do livro"""
	pi = 0
	for k in range(n):
		pi += pow(-3, -k) / (2*k+1)
	pi *= math.sqrt(12)
	print('pi = ', pi)
#	print('error = ', abs(pi - math.pi))

madhava_livro(20)
