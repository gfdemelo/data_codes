#!/usr/bin/env python3


def is_palindrome(a):
	if a[::-1] == a[:]:
		print(a, 'é um palindromo')
		return True
	else:
		print(a, 'não é um palindromo')
		return False

is_palindrome('reviver')
