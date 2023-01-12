#!/usr/bin/env python3



def rotate_word(a, t):
	a.lower()
	w=''
	for i in a:
		conv=ord(i)+t
		if conv >= 122:
			conv = conv -26
			w=w+(chr(conv))
		elif conv <= 97:
			conv= conv+26
			w=w+(chr(conv))
		else:
			w=w+(chr(conv))
	return w


#print(rotate_word('abcd', -7))
	
