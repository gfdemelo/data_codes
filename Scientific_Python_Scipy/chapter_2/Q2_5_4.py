#!/usr/bin/env python

c=input('Números de carbonos: ')

def alkanes(s):
	print('H3C', end='-')
	for i in range(int(s)-2):
		print('CH2', end='-')
	print('CH3')
	print('\n')
alkanes(c)	
