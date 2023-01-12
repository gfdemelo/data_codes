#!/usr/bin/env python3


#x = int(input('Qual o valor de um dos lados do triângulo? '))
#y = int(input('Qual o valor de um dos lados do triângulo? '))

import math


def hypotenuse(a, b):
	c=a**2+b**2
	hipotenusa=math.sqrt(c)
	print(hipotenusa)
	return hipotenusa


hypotenuse(3,4)
