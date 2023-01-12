#!/usr/bin/env python

import numpy as np

n, x = 60, 0.0107 #n é número de carbonos no fulereno e x a abundancia do 13C
mmax = 4
m = np.arange(mmax+1)

#Estimativa da abundancia por amostragem aleatoria da distribuição binomial
ntrials = 10000
pbin = np.empty(mmax+1)

#Para cada valor de r em m, amostramos um grande número de vezes(ntrials) da distribuição binomial descrita por n=60 e probabilidade, x = 0.0107. A comparação desses valores com um dado valor de r gera um array booleano que pode ser somado(True=1,False=0). A divisao por dá uma estimativa da probabilidade de exatamente r atomos sendo do tipo 13C e o restante 12C.

for r in m:
	pbin[r] = np.sum(np.random.binomial(n, x, ntrials)==r)/ntrials

#Cacular e armazenar os coeficientes binomiais nCm
nCm = np.empty(mmax + 1)
nCm[0] = 1
for r in m[1:]:
	nCm[r] = nCm[r-1] * (n-r+1)/r

#A resposta exata da distribuiçao binomial
p = nCm * x**m * (1-x)**(n-m)

print('Abundances of C60 as (13C) [m] (12C) [60-m]')
print('m    "Exact"     Estimated')
print('-'*24)
for r in m:
	print('%.1d    %6.4f      %6.4f' %(r, p[r], pbin[r]))
