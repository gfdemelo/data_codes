#!/usr/bin/env python3


from  ex12_2_1 import anagrama

arq=open('words.txt')
word=input('Digite palavra para procurar anagrama: ')

def read_anagrams(word, t):
	for item in anagrama(t):
		if word==item:
			print(item)
		for index in item:
			if word==index:
				print(item)

read_anagrams(word,arq)
	

