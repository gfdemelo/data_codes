#!/usr/bin/env python3


def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) <= 1:
		print('True')
		return True
	elif first(word) == last(word): 
		if int(len(middle(word))) % 2 == 0 :
			a=is_palindrome(middle(word))
			return a
		else:
			return is_palindrome(middle(word))
	else:
		print('False')
		return False	
	
is_palindrome('omississimo')
		
