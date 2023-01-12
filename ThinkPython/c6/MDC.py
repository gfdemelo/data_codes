#!/usr/bin/env python3

def gcd(a, b):
	if a < b:
		return gcd(b, a)
	elif b == 0:
		print('O MDC é ', a)
		return a
	else:
		r = a%b
		return gcd(b, r)
	
gcd(24, 16)
		
