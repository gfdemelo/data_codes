#!/usr/bin/env python3

def is_power(a, b):
	if a == 1 or b ==1:
		print('True')
		return True
	elif a % b == 0:
		c=a/b
		return is_power(c, b)
	
	else:
		print('False')
		return False


is_power(15,4)
		
		
