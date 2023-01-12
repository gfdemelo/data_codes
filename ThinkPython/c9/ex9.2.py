#!/usr/bin/env python3

arq=open('words.txt')


def has_no_e(t):
	for line in t:
		if line == 'e':
#			print('Esta palavra possui a letra E')
			return False
	print(t)	
#	print('Esta palavra não possui a letra E')
	return True






def count_words(t):
	words=0
	words_e=0
	for line in arq:
		words=words+1
		a=line.strip()
		if has_no_e(a):
			words_e=words_e+1
	print('A porcentagem de palavras sem a letra E é: ', words_e*100/words)

		
count_words(arq)
