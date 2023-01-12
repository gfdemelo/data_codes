#!/usr/bin/env python3


a = int(input('Digite um números inteiro para base: '))
b = int(input('Digite um números inteiro para base: '))
c = int(input('Digite um números inteiro para base: '))
n = int(input('Digite um números inteiro para expoente: '))


def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print('Holy smokes, Fermat was wrong!')
	elif n <= 2 and a**n + b**n == c**n:
		print('This works!')
	else:
		print("No, that's doesn't work!")

check_fermat(a, b, c, n)

			
