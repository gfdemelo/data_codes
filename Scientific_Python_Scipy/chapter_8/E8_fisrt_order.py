#!/usr/bin/env python

import numpy as np
import pylab
from scipy.integrate import odeint

#Reação de primeira ordem com constante de velocidade em s-1
k = 0.2
#Condição inicial em y: 100% dos reagentes estão presentes em t=0
y0 = 100

#Grid de pontos de tempo para a reação
t = np.linspace(0, 20, 20)

def dydt(y, t):
	return -k * y

#Integra a equação diferencial
y = odeint(dydt, y0, t)

#plota e compara as soluções numerica e exata
pylab.plot(t, y, 'o', color='k', label=r'\texttt{odeint}')
pylab.plot(t, y0*np.exp(-k*t), color='gray', label='Exact')
pylab.xlabel(r'$t\;/\mathrm{s}$')
pylab.ylabel('Remaining reactant (\%)')
pylab.legend()
pylab.show()

