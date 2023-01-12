#!/usr/bin/env python


import numpy as np
from numpy.polynomial import Polynomial
import pylab

#Volume do líquido no tanque esférico: V = pi*(Raio)*(altura**2) - 1/3*pi*(altura**3)
#Fluxo constante do líquido: F = -dV/dt
#Diferenciando altura com relação a t: (2pi*(raio)*(altura) - pi*(altura**2)dh/dt = -F
#Se iniciarmos com tanque cheio (altura = 2*raio) em t=0, essa equação pode ser integrada.
#Resulta no polinômio: -1/3*pi*(altura**3) + pi*(raio)*(altura**2) + (F*t - 4/3*pi*(raio**3))=0


#Raio do tanque esférico em m
R = 1.5
#Fluxo de saída do tanque , m^3.s-1
F = 2.E-4
#Volume total do tanque, m^3
V0 = 4/3*np.pi*R**3
#Tempo total para o tanque se esvaziar
T = V0 / F

#coeficientes dos termos quadráticos e cúbicos do polinômio da altura
c2,c3 = np.pi*R, -np.pi/3

N=100
#array de N pontos de tempo entre t=0 e t=T
time = np.linspace(0,T,N)
#criando o array correspondente de alturas
h = np.zeros(N)
for i, t in enumerate(time):
	c0 = F*t - V0
	p = Polynomial([c0,0,c2,c3])
	#encontra as raízes desse polinônio
	roots = p.roots()
	#queremos uma raiz para cada 0 <= h <= 2R
	h[i] = roots[(0 <= roots) & (roots <= 2*R)][0]

pylab.plot(time, h, 'o')
pylab.xlabel('Time /s')
pylab.ylabel('Altura do tanque /m')
pylab.show()





