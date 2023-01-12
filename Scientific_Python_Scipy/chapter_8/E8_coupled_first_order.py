#!/usr/bin/env python

import numpy as np, pylab
from scipy.integrate import odeint

#Constantes de primeira ordem, s-1
k1, k2 = 0.2, 0.8
#Condição inicial em y1, y2: [A] (t=0) = 100, [B](t=0)=0
A0, B0 = 100, 0

#Grid de pontos de tempo
t = np.linspace(0, 20, 100)

def dydt(y, t, k1, k2):
	y1, y2 = y
	dy1dt = -k1 * y1
	dy2dt = k1 *y1 - k2 * y2
	return dy1dt, dy2dt

#Integração de diferencial
y0 = A0, B0
y1, y2 = odeint(dydt, y0, t, args=(k1, k2)).T
A, B = y1, y2
#[P] é determinado por
P = A0 - A - B

#Resultado analítico
Aexact = A0 * np.exp(-k1*t)
Bexact = A0 * k1/(k2-k1) * (np.exp(-k1*t) - np.exp(-k2*t))
Pexact = A0 - Aexact - Bexact

pylab.plot(t, A, 'o', label='[A]')
pylab.plot(t, B, '^', label='[B]')
pylab.plot(t, P, 'd', label='[P]')
pylab.plot(t, Aexact)
pylab.plot(t, Bexact)
pylab.plot(t, Pexact)
pylab.xlabel(r'$t\;/\mathrm{s}$')
pylab.ylabel('Concentration (arb.units)')
pylab.legend()
pylab.show()



