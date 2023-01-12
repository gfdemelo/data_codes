#!/usr/bin/env python


import numpy as np
from numpy.polynomial import Polynomial
import pylab


dados1 = np.genfromtxt('ex6-4-a-anscombe.txt', dtype=float, usecols=(0,1))
dados2 = np.genfromtxt('ex6-4-a-anscombe.txt', dtype=float, usecols=(2,3))
dados3 = np.genfromtxt('ex6-4-a-anscombe.txt', dtype=float, usecols=(4,5))
dados4 = np.genfromtxt('ex6-4-a-anscombe.txt', dtype=float, usecols=(6,7))

dados = np.array((dados1.T, dados2.T, dados3.T, dados4.T))
#print(dados)
print('Média x | Variância x | Coef. Corr. x | Média y | Variância y | Coef. Corr y| rms |Equação linear ')


for item in dados:
	dmin, dmax = min(item[0]), max(item[0])
	#print(item[0])	
	pfit, stats = Polynomial.fit(item[0], item[1], deg=1, full=True, window=(dmin, dmax), domain=(dmin, dmax))
	lin, coeff = pfit
	resid, rank,  sing_val, rcond = stats
	print('%.5f |  %.5f   | %.5f       | %.5f | %.5f     | %.5f     | %.3f  | y = %.5f x + %3.f' % (item[0].mean(), item[0].var(), np.corrcoef(item[0]), item[1].mean(), item[1].var(), np.corrcoef(item[1]), np.sqrt(resid[0]/len(item[1])), coeff, lin))
	pylab.plot(item[0], item[1], 'o', color='r')
	pylab.plot(item[0], pfit(item[0]), color='k')
	pylab.xlabel('x')
	pylab.ylabel('y')
	pylab.show()
	
