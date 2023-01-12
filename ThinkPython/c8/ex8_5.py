#!/usr/bin/env python3



def rotate_word(a, t):
	a.lower()
	for i in a:
		conv=ord(i)+t
		if conv >= 122:
			conv = conv -26
			print(chr(conv), end='')
		elif conv <= 97:
			conv= conv+26
			print(chr(conv), end='')
		else:
			print(chr(conv), end='')
	print('\n')


rotate_word('abcd', -7)
	
