#!/usr/bin/env python



def count(word, letter):
	count=0
	for letra in word:
		if letra == letter:
			count = count+1
	print('O número de vezes que', letter, 'aparece em', word, 'é', count)
	return count

count('assassino', 's')

