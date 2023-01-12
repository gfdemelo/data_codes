#!/usr/bin/env python

import numpy as np
import pylab
from numpy.polynomial import Polynomial


#dados: conc = [P] e absorbância, A

conc = np.array([0,20,40,80,120,180,260,400,800,1500])
A = np.array([2.287, 3.528, 4.336, 6.909, 8.274, 12.285, 16.085, 24.797, 49.058, 89.400])

cmin, cmax = min(conc), max(conc)

pfit, stats = Polynomial.fit(conc, A, deg=1, full=True, window=(cmin,cmax), domain=(cmin, cmax))

print('Resultados do fit', pfit, stats, sep='\n')

A0, m = pfit
resid, rank, sing_val, rcond = stats
rms = np.sqrt(resid[0]/ len(A))

print('Fit: A = %.3f [P] + %.3f, rms residual %.4f' % (m, A0, rms))

pylab.plot(conc, A, 'o', color='k')
pylab.plot(conc, pfit(conc), color='k')
pylab.xlabel('[P] /$\mathrm{\mu g\cdot mL^{-1}}$')
pylab.ylabel('Absorbância')
pylab.show()
