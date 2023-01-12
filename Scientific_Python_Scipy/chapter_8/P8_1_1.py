#!/usr/bin/env python

from scipy.special import binom

n=8

def Pascal_triangle(f):
	for n in range(f):
		for k in range(n+1):
			print(int(binom(n,k)), end=' ')
		print('\n')

Pascal_triangle(8)
		
		
