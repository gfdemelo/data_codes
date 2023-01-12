#!/usr/bin/env python


import numpy as np, pylab
from scipy.integrate import odeint

#Frequencia do oscilador harmonico (s-1)
omega = 0.9
#Condições iniciais em x1=x r x2=dx/dt em t=0
A, v0 = 3, 0 		#cm, cm.s-1
x0 = A, v0

#Grid de tempos
t = np.linspace(0, 20, 100)

def dxdt(x, t, omega):
	x1, x2 = x
	print(x)
	dx1dt = x2
	dx2dt = -omega**2 * x1
	print(dx1dt, dx2dt)
	return dx1dt, dx2dt

x1, x2 = odeint(dxdt, x0, t, args=(omega,)).T

pylab.plot(t, x1, 'o', color='k', label=r'\texttt{odeint()}')
pylab.plot(t, A * np.cos(omega*t), color='gray', label='Exact')
pylab.xlabel('t / s')
pylab.ylabel('x / cm')
pylab.legend()
pylab.show()
