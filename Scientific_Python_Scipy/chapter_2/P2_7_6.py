#!/usr/bin/env python


import math

def double_fatorial(t):
	return 1 if t==0 or t==1 else double_fatorial(t-2)*t

def sinm_cosn(m,n):
	if m>1 and n> 1:
		if m % 2 ==0 and n%2==0:
			return (double_fatorial(m-1)*double_fatorial(n-1)*math.pi)/(2*double_fatorial(m+n))
		else:
			return (double_fatorial(m-1)*double_fatorial(n-1))/(double_fatorial(m+n))		
	else:
		raise ValueError()

print(sinm_cosn(1,4))
	
