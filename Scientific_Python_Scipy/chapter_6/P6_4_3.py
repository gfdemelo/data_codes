#!/usr/bin/env python


import numpy as np
from numpy.polynomial import Polynomial
import pylab


#a e b são constantes de vanderwalls da Amônia
a = 4.225 #L^2 bar mol^-2
b = 0.03707 #L mol^-1
R1 = 8.314 #J K^-1 mol^-1
R2 = 0.082 #atm L mol^-1 K^-1, 1 atm = 1.01325 bar

#Temperatura crítica
Tc = 8*a / (27*R2*b)
#Pressão crítica
Pc = a / (27*b**2)
#pV^3 - (pb + RT)V^2 + aV - ab = 0
T1 = 298 #K
T2 = 500 #K
P1 = 1 #atm
P2 = 111.51 # atm = 12 MPa
p1 = Polynomial([-a*b, a, -P1*b-R2*T1, P1]).roots()
p2 = Polynomial([-a*b, a, -P2*b-R2*T2, P1]).roots()


print('O ponto crítico da Amônia é (%.5f K, %.5f atm)' % (Tc*1.01325,Pc*1.01325))
print('O volume molar V é %.3f a 298K/1atm e %.3f a 500K/12MPa' % (p1[2], p2[2].real))

#Isoterma
T3 = 350 #K
vmin, vmax = 0.1, 2
V = np.linspace(vmin,vmax,201)
P = (R2*T3)/(V - b) - 1.01325*a/(V**2)
P_ideal = R2*T3/V
pylab.plot(V, P, color='r', label='Van der Walls')
pylab.plot( V, P_ideal, color='b', label='Gás ideal')
pylab.xlabel('V (L mol $\mathrm{L^{-1}}$)')
pylab.ylabel('P (atm)')
pylab.title('Isoterma - 350K - NH$\mathrm{_3}$')
pylab.legend()
pylab.show()
