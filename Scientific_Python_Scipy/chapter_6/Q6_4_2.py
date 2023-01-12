#!/usr/bin/env python

import numpy as np
from numpy.polynomial import Polynomial

#f(x) = (x^2 + x - 11)^2 + (x^2 + x - 7)^2. Qual os pontos estácionários (de inflexão)?
#Os pontos estácionários são aqueles em que f'(x) = 0


f1 = Polynomial([-11, 1, 1])
f2 = Polynomial([-7, 1, 1])
f = f1**2 + f2**2
d1 = f.deriv().roots() #pontos estacionários
d2 = f.deriv(2)
minima = d1[d2(d1) >0]
maxima = d1[d2(d1) < 0]

print('Os pontos estácionários são: (%.3f, %.3f), (%.3f, %.3f),(%.3f, %.3f)' % (d1[0], f1(d1[0]), d1[1], f(d1[1]), d1[2], f(d1[2])))
print('Os pontos de mínimo são: ', np.array([minima, f(minima)]).T)
print('O ponto de máximo é: ', np.array([maxima, f(maxima)]).T)
