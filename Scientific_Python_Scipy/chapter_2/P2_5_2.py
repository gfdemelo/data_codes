#!/usr/bin/env python

import math

def concentration(c,K):
	H,tol=0,1
	while tol > 1.E-10:
		i=H
#		print('i =', i, end=' - ')
		H=math.sqrt(K*(c-H)) 
		tol=abs(H-i)
#		print('tol =', tol)
	return H

a=concentration(0.001,1.78E-5)
print('pH = %f' % (math.log(a,10)*(-1)))
