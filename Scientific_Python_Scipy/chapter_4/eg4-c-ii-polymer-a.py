#!/usr/bin/env python

#Compara a distribuição das distâncias end-to-end com a predita teoricamente pela função de densisade de probabilidade
# P(R) = 4*pi*R**2(3/2pi*<r**2>)^3/2 * exp(-3R**2/2<r**2>), em que, <r**2> = Na**2, a posição média quadrada do segmento


import pylab
from polymer import Polymer

#Calcula R para Np polimeros
Np = 3000

#Cada polímero consiste de N segmentos de comprimento a
N, a = 1000, 1.
R = [None] * Np
for i in range(Np):
	polymer = Polymer(N, a)
	Rx, Ry, Rz = polymer.R
	R[i] = pylab.sqrt(Rx**2 + Ry**2 + Rz**2)
	# Retorna um indicador de progresso a cada 100 polimeros
	if not (i+1) % 100:
		print(i+1, '/', Np)

#Plot a distribuição de Rx como um histograma normalizado usando 50 bins

pylab.hist(R, 50, normed=1)

#Plot a distribuição de probabilidade, Pr, uma função de r

r = pylab.linspace(0, 200, 1000)
msr = N * a**2
Pr = 4.*pylab.pi*r**2 * (2 * pylab.pi * msr / 3)**-1.5 * pylab.exp(-3*r**2/2/msr)
pylab.plot(r, Pr, lw=2, c='r')
pylab.xlabel('R')
pylab.ylabel('P(R)')
pylab.show()
