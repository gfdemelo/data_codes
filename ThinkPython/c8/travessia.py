#!/usr/bin/env python3



def travessia(a):
	index=1
	while index < len(a)+1:
		letter=a[-index]
		print(letter)
		index=index+1

travessia('gabriel')
