#!/usr/bin/env python



def count(word, letter, index):
	count=0
	while index < len(word):
		if word[index] == letter:
			count = count+1
			index=index+1
		else:
			index=index+1
	print('O número de vezes que', letter, 'aparece em', word, 'é', count)
	return count

count('assassino', 's', 2)

