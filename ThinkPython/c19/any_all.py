#!/usr/bin/env python3

def uses_all(word, required):
	return all(letter in required for letter in word)


print(uses_all('gabriel', 'abcdefghiklmn'))
