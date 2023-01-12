#!/usr/bin/env python

import math

def powr(a, b):
	if a==0 and b==0:
		raise ValueError('O número não pode ser zero')
	else:
		return math.pow(a,b)

#COM ASSERT

def powr2(a, b):
		
	assert b != 0 or a!= 0, 'O número não pode ser zero'
	return math.pow(a,b)






print(powr2(0,0))
