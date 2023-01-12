#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad, odeint
import matplotlib.pyplot as plt

k1 = 3e-12		#O_2 + hv = 2O
k2 = 1.2e-33		#O_2 + O + M = O_3 + M
k3 = 5.5e-4		#O_3 + hv = O + O_2
k4 = 6.9e-16		#O + O_3 = 2O_2

M = 9e17
O2_0, O_0 ,O3_0 = 0.21*M, 0, 0
O_initial = O_0, O2_0, O3_0
t = np.linspace(0, 10**8, 10**5)




def dodt(O_all, M, t):
	O, O2, O3 = O_all
	dO2 = -k1*O2 - k2*O2*O*M + k3*O3 + 2*k4*O*O3
	dO3 = k2*O2*O*M - k3*O3 - k4*O*O3
	dO = 2*k1*O2 - k2*O2*O*M + k3*O3 - k4*O*O3
	return dO, dO2, dO3 


O, O2, O3 = odeint(dodt, O_initial, t, args=(M,)).T

#Aproximação
O3_approx = np.sqrt((k1*k2)/(k3*k4))*O2[-1]*M**0.5
print(O3[-1], O3_approx)
O_O3_approx = k3/(k2*O2[-1]*M)
print(O[-1]/O3[-1],O_O3_approx)





fig, axes = plt.subplots(nrows=3, ncols=1)
ax1=axes[0]
ax2=axes[1]
ax3=axes[2]

ax1.plot(t,O, label='[O]', c='g')
ax1.set_xticks([])
ax1.legend()

ax2.plot(t,O2, label='[O$\mathrm{_2}$', c='r')
ax2.set_xticks([])
ax2.legend()

ax3.plot(t,O3, label='[O$\mathrm{_3}$', c='b')
ax3.set_xlabel('t / s')
plt.legend()
plt.show()
