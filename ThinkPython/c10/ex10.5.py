#!/usr/bin/env python3



def is_sorted(t):
	if t == sorted(t):
		print('True')
		return True
	else:
		print('False')
		return False

a=[1,2,3,4,5]
b=[1,3,4,2,5]

is_sorted(b)	
