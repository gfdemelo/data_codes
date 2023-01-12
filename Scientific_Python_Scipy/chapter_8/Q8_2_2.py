#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad
from scipy.special import i0

# A
a = quad(lambda x: (x**4 * (1-x)**4)/(1 + x**2), 0, 1)
print('Letra A')
print('integral = ', a[0], 'compared with 22/7 - pi = ', 22/7 - np.pi)
print('\n')

#B
b = quad(lambda x: x**3 / (np.exp(x) - 1), 0, np.inf)
print('Letra B')
print('integral = ', b[0], 'compared with pi^4/15 = ', np.pi**4/15)
print('\n')

#C
c = quad(lambda x: x**-x, 0, 1)
print('Letra C')
print('integral = ', c[0], 'compared with sum(n^-n)^inf n=1 = ', np.sum(n**-n for n in range(1,50)))
print('\n')

#D
print('Letra D')
def func_d(x, n):
	return (np.log(1/x))**n
for p in range(1,11):
	print(quad(func_d, 0, 1, args=(p))[0], np.math.factorial(p))
print('\n')

#E
def func_e(x, f):
	return np.exp(f*np.cos(x))

z = np.linspace(0, 2, 100)
for number in z:
	d = (quad(func_e, 0, 2*np.pi, args=(number))[0], 2*np.pi*i0(0, z))
print(d[0])
