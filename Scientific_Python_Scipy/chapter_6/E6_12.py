#!/usr/bin/env python


import numpy as np, pylab

#Lei de Beer-Lambert (relaciona a concentração da amostra à intensidade da luz transmitida)
#	I_t = I_0 * exp(-a*c*l)  
#I_0 é a intensidade da luz incidente
#a é o coeficiente de absorção, c é conc. e l o comprimento do path
# y = ln(I_t/I_0) = -a*c*l
# y = mc + k

path = 0.8 #cm
conc = np.array([0.4,0.6,0.8,1.0,1.2])
It_I0 = np.array([0.886, 0.833, 0.784, 0.738, 0.694])

n = len(conc)
A = np.vstack((conc, np.ones(n))).T
T = np.log(It_I0)

x, resid, _, _ = np.linalg.lstsq(A, T) #_ são dummies variaveis que não serao usadas
m, k = x
a = -m/path
print('a = %.3f M-1.cm-1' % (a))
print('k =', k)
print('rms residual = ', np.sqrt(resid[0]))

pylab.plot(conc, T, 'o')
pylab.plot(conc, m*conc + k)
pylab.xlabel('$conc\;/\mathrm{M}$')
pylab.ylabel('$\ln(I_\mathrm{t}/I_0)$')
pylab.show()

