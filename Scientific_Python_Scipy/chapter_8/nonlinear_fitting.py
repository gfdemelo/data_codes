#!/usr/bin/env python


import numpy as np, pylab
from scipy.optimize import leastsq

#Fitting com os mínimos quadrados sendo f(t) = A*exp(t/tau) * cos2*pi*ni*t

A, freq, tau = 10, 4, 0.5

def f(t, A, freq, tau):
	return A * np.exp(-t/tau) * np.cos(2*np.pi*freq*t)


tmax, dt = 1, 0.01
t = np.arange(0,tmax, dt)
yexact = f(t, A, freq, tau)
y = yexact + np.random.randn(len(yexact))*2
pylab.plot(t, yexact,color='r', label='Exact')
pylab.scatter(t,y, color='k', label='Data')


#Fitando os ruídos de y aos parâmetros A, freq, tau
def residuals(p, y, t):
	A, freq, tau = p
	return y - f(t, A, freq, tau)

#Chute inicial para os parâmetros que não estão tão fora

p0 = 5, 5, 1
plsq = leastsq(residuals, p0, args=(y,t))
pfit=plsq[0]
print(pfit)
pylab.plot(t, f(t, *pfit), c='green', label='Fit')
pylab.legend()
pylab.show()

