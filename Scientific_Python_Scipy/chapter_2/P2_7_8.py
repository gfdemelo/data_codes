#!/usr/bin/env python

def tetration(n,x):
	if n==1:
		return x**x
	return tetration(n-1,x)**x

print(tetration(3,3))
