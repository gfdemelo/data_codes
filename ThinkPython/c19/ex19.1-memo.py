#!/usr/bin/env python3


known_n={0:0}
known_k={0:1}

def binomial_coeff(n, k):
	"""Computa o coeficiente binomial "n escolhe k"
	n: número de tentativas
	k: número de sucessos 
	returns: int """

	return known_k[k] if k in known_k else known_n[n] if n in known_n else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)

n=int(input('digite n: '))
k=int(input('digite k: '))
print(binomial_coeff(n, k))
