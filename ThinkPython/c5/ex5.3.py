#!/usr/bin/env python3


a = int(input('Digite o comprimento de um dos lados do triângulo: '))
b = int(input('Digite o comprimento de um dos lados do triângulo: '))
c = int(input('Digite o comprimento de um dos lados do triângulo: '))

def is_triangle(a, b, c):
	if a+b<c or a+c<b or b+c<a:
		print('Não é possível formar um triângulo')
	elif a+b==c or a+c==b or b+c==a:
		print('É possível formar um triângulo degenerado')
	else:
		print('Sim, é possível formar um triângulo com esses lados')


is_triangle(a, b, c)	
			
