#!/usr/bin/env python

import numpy as np
from numpy.polynomial import Polynomial
import pylab

x = np.array([1.3, 6.0, 20.2, 43.9, 77.0, 119.6, 171.7, 233.2, 304.2, 384.7, 474.7, 574.1, 683.0, 801.3, 929.2, 1066.4, 1213.2, 1369.4, 1535.1, 1710.3, 1894.9])

dt, tmax, n = 0.1, 0.1*(len(x)-1), len(x)

t = np.linspace(0, tmax, n)
A = np.vstack((np.ones(n), t, t**2)).T
coeff, resid, _, _ = np.linalg.lstsq(A, x)
x0, v0, g = coeff[0], coeff[1], coeff[2] *2/100 		#Posição inicial em cm, velocidade em cm.s-1, e gravidade em m.s-2

print('x0 = %.3f cm, v0 = %.3f cm.s-1, g = %.3f m.s-2' % (x0, v0, g))
print('rms residual = ', resid[0])

xfit = Polynomial(coeff)(t)  #funçao polinomial com coeficientes coeff e a variavel t substituida pelos valores de t

pylab.plot(t, x, 'o')
pylab.plot(t, xfit, 'b')
pylab.xlabel('Time (sec)')
pylab.ylabel('Distance (cm)')
pylab.show()

