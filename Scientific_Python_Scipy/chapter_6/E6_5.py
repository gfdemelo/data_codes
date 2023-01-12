#!/usr/bin/env python

""" Define um array 2D com valores das funções oscilandoras x(L - x)sin(2pi*x/lambda_n), sendo lambda_n = 2L/n (n = 1,2,3 ...), para L = 1 em um grid de N = 100 pontos (linhas) para n = 1,2 ... 5 (colunas). """


import numpy as np
import pylab

N = 100
L = 1

def f(i,n):
	x = i * L/N
	lam = 2 * L/(n+1)
	return x * (L-x) * np.sin(2*np.pi*x/lam)


a = np.fromfunction(f, (N+1,5))
print(a)
min_i = a.argmin(axis=0)
max_i = a.argmax(axis=0)
pylab.plot(a, c = 'k')
pylab.plot(min_i, a[min_i, np.arange(5)], 'v', c = 'k', markersize=10)
pylab.plot(max_i, a[max_i, np.arange(5)], '^', c = 'k', markersize=10)
pylab.xlabel(r'$x$')
pylab.ylabel(r'$f_n(x)$')
pylab.show()
