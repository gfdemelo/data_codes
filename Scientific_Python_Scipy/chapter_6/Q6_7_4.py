#!/usr/bin/env python

import numpy as np

#Livro de 500 páginas com misprints, qual a probabilidade de que uma página tenha 2 ou mais misprints

#Binomial
m,n, ntrials=400,500, 100
a = np.random.binomial(m, 1/n, (ntrials, n))
b = [(np.sum(a>=2))/n/ntrials]
print(b)
