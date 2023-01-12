#!/usr/bin/env python3


import math

def fatorial(n):
	if n == 0:
		return 1
	result=n*fatorial(n-1)
	return result



def estimate_pi():
	soma=0
	k=0
	total=0
	while True:
		soma=((fatorial(4*k))*(1103+26390*k))/(((fatorial(k))**4)*(396**(4*k)))
		total=soma+total
		resultado=total*2*math.sqrt(2)/9801
		k=k+1
		if abs(soma) < 1e-15:
			pi=1/resultado
			return pi


print(estimate_pi())
