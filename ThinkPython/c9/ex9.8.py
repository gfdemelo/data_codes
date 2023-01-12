#!/usr/bin/env python3


#user=input('Digite seis numeros: ')

def number_palindrome(a):
	i=0
	while i < len(a)-1:
		if a[i:len(a)] in a[::-1]:
		#	print(a)
			return True
		i=i+1
	return False

def check():
	i=100000
	while i <= 999999:
		if number_palindrome(str(i)):
			print(i)
		i=i+1
	

check()	
	
	
