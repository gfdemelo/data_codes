#!/usr/bin/env python


import numpy as np
from  numpy.polynomial import Polynomial
from scipy.optimize import minimize
from  scipy.integrate import quad

ordem = [1,2,3,4]

def wave(x,N):
	psi_trial=0
	for n in range(N+1):
		phi = Polynomial([1,-1])**(N-n+1)
		phi2 = Polynomial([1, 1])**(n+1)
		psi_trial += phi*phi2
	E_upper = quad(psi_trial * psi_trial.deriv(2), -x,x)
	E_lower = quad(psi_trial * psi_trial,-x,x)
	return E_upper[0]/E_lower[0]

for N in ordem:
	minima = minimize(wave,1, args=(N))['fun']
	print('N = %.1d, E_exact = %.5f, E_estimated = %.5f' %(N,wave(1,N),minima))
 
