#!/usr/bin/env python3


def is_anagram(t, a):
	x=list(t)
	y=list(a)
	for item in x:
		if item not in y:
			print('False')
			return False
		else:	
			print('True')
			return True
#uma outra maneira em is_anagram é return sorted(t) == sorted(a)

t='eroma'
a='amorf'
is_anagram(t, a)
