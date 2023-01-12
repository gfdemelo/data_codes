#!/usr/bin/env python


number = int(input('Digite um número inteiro maior que zero: '))

def hailstone(n):
	print(n)
	if n==1:
		return "end"
	if n % 2 == 0:
		return hailstone(n/2)
	if n %2 != 0:
		return hailstone(3*n+1)

hailstone(number)
