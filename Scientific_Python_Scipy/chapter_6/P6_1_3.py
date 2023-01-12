#!/usr/bin/env python


import numpy as np
import pylab 

	

n = 1000
xmin, xmax = -10,10
desvio = np.array([[0.5],[1],[1.5]])
media = 0
x = pylab.linspace(xmin, xmax, n)
a = np.fromfunction(lambda n,:(1/(desvio*pylab.sqrt(2*pylab.pi)))*pylab.exp(-((x - media)**2)/(2*desvio**2)), (n,))

print('Normalização = ',np.sum(a/np.sum(a)))

pylab.title('Gaussian Function')
pylab.plot(x,a[0], color='magenta', linestyle='-', label='σ = 0.5')
pylab.plot(x,a[1], color='black', linestyle='-', label='σ = 1')
pylab.plot(x,a[2], color='blue', linestyle='-', label='σ = 1.5')


#Cálculo primeira derivada
h = 0.001
a1 = np.fromfunction(lambda n,:(1/(desvio*pylab.sqrt(2*pylab.pi)))*pylab.exp(-(((x+h) - media)**2)/(2*desvio**2)), (n,))
a2 = np.fromfunction(lambda n,:(1/(desvio*pylab.sqrt(2*pylab.pi)))*pylab.exp(-(((x-h) - media)**2)/(2*desvio**2)), (n,))

g = np.fromfunction(lambda n,: ((a1)-(a2))/(2*h), (n,))
pylab.plot(x,g[0], color='magenta', linestyle='--', label='σ\' = 0.5')
pylab.plot(x,g[1], color='black', linestyle='--', label='σ\' = 1')
pylab.plot(x,g[2], color='blue', linestyle='--', label='σ\' = 1.5')
pylab.legend()
pylab.show()
