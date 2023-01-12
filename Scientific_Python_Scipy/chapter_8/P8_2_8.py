#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad, dblquad, odeint
import matplotlib.pyplot as plt


k1 = 1.816e-5 		#s-1	212_P = 212_Bi + beta-
k2 = 6.931e-5		#s-1	212_Bi = 208_Tl + alpha
k3 = 1.232e-4		#s-1	212_Bi = 212_Po +beta-
k4 = 3.851e-3		#s-1	208_Tl = 208_Pb + beta-
k5 = 2.310		#s-1	212_Po = 208_Pb + alpha

P_0, Bi_0, Tl_0, Po_0, Pb_0 = 1, 0, 0, 0, 0
decay_in = P_0, Bi_0, Tl_0, Po_0, Pb_0

t = np.linspace(0, 3e5, 10**2)

def ddt(conc, t):
	P, Bi, Tl, Po, Pb = conc
	dP = -k1*P
	dBi = k1*P - k2*Bi - k3*Bi
	dTl = k2*Bi - k4*Tl
	dPo = k3*Bi - k5*Po
	dPb = k4*Tl + k5*Po
	
	return dP, dBi, dTl, dPo, dPb

P, Bi, Tl, Po, Pb = odeint(ddt, decay_in, t).T
#print(P, Bi, Tl, Po, Pb) 


fig=plt.figure()
ax = fig.add_subplot(111)

ax.plot(t, P, label='$\mathrm{^{212}Pb}$')
ax.plot(t, Bi,label='$\mathrm{^{212}Bi}$')
ax.plot(t, Tl,label='$\mathrm{^{208}Tl}$')
ax.plot(t, Po,label='$\mathrm{^{212}Po}$')
ax.plot(t, Pb,label='$\mathrm{^{208}Pb}$')
ax.plot(t, P_0*(1-np.exp(-k1*t)), label='approx $\mathrm{^{208}Pb}$')
ax.set_xlabel('t / s')
ax.set_ylabel('concentration')
ax.grid(ls='--', lw=0.5)
ax.set_title('Concentration x time for $\mathrm{^{212}P}$ decay')
plt.legend()
plt.show()





