#!/usr/bin/env python3


def has_duplicates(t):
	i=0
	while i+1 < len(t):
		a=sorted(t)
		if a[i]==a[i+1]:
			print('True')
			return True
		else:
			i=i+1
	print('False')
	return False


x=[1,2,4,3,4]
has_duplicates(x)
			
