#!/usr/bin/env python

import math

def agm(x,y):
	tol=1.0E-14
	a,b=x,y
	while abs(a-b) > tol:
		a,b=(a+b)/2,math.sqrt(a*b)
	return a	

print('A constante de Gaussian é %.14f ' % (1/agm(1,math.sqrt(2))))
