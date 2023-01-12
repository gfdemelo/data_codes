#!/usr/bin/env python3


#known={0:0}
#known2={0:1}

def binomial_coeff(n, k):
	"""Computa o coeficiente binomial "n escolhe k"
	n: número de tentativas
	k: número de sucessos 
	returns: int """

	return 1 if k == 0 else 0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)

n=int(input('digite n: '))
k=int(input('digite k: '))
print(binomial_coeff(n, k))
