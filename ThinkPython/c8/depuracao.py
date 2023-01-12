#!/usr/bin/env python3

def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False
	i =0
	j=len(word2)-1
	while j>=0:
		if word1[i] != word2[j]:
			print('False')
			return False
		print(i, j)
		i=i+1
		j=j-1
	print('True')
	return True


is_reverse('stop', 'pots')
