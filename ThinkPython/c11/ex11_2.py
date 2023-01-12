#!/usr/bin/env python3

hist={'a':1, 'p':1, 'r':2, 't':1, 'o':1}



def invert_key(d):
	inverse=dict()
	for key in d:
		inverse.setdefault(d[key], []).append(key)
	return inverse 


print(invert_key(hist))
		
