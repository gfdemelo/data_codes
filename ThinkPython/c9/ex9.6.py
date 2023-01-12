#!/usr/bin/env python3



a=input('Digite uma palavra: ')


def is_abecedarian(t):
		i=0
		while i <= len(t)-2:
			if ord(t[i]) > ord(t[i+1]):    #poderia fazer sem ord, apenas com t[i]
				print('False')
				return False
			else:
				i=i+1
		print('True')
		return True

is_abecedarian(a)



