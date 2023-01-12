#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#A equação de difusao unidimensional aplicada a temperatura de duas barras de metais diferentes

#Cross-sectional area of bar in m3, heat added at x=0 in J
A, H = 1.e-4, 1.e3
#Temperature in K at x=0
theta0 = 300

#MEtal elemen symbol, specific heat capacities per unit of volume (J.m-3.K-1), Thermal diffusivities (m2.s-1) for Cu and Fe
metals = np.array([('Cu', 3.45e7, 1.11e-4), ('Fe', 3.50e7, 2.3e-5)], dtype=[('symbol', '|S2'), ('cp', 'f8'), ('D', 'f8')])

#The metal bar extends from -xlim to xlim(m)
xlim, nx = 0.05, 1000
x = np.linspace(-xlim, xlim, nx)

#Calculate the temperature distribution at these three times
times = (1e-2, 0.1, 1)
#Creates out subplots:  three rows of times, one column for each metal
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(7,8))
for j, t in enumerate(times):
	for i, metal in enumerate(metals):
		symbol, cp, D = metal
		ax = axes[j, i]
		#The solution to the diffusion equation
		theta = theta0 + H/cp/A/np.sqrt(D*t) / 4/np.pi*np.exp(-x**2/4/D/t)
		#Plot, converting distances to cm and add some labelling
		ax.plot(x*100, theta, 'k')
		ax.set_title('{}, $t={}$ s'.format(symbol.decode('utf8'), t))
		ax.set_xlim(-4, 4)
		ax.set_xlabel('$x\;/\mathrm{K}$')

#Set up the y axis so that each metal has the same scale at the same t
for j in (0,1,2):
	ymax = max(axes[j,0].get_ylim()[1], axes[j,1].get_ylim()[1])
	for i in (0,1):
		ax=axes[j,i]
		ax.set_ylim(theta0, ymax)
		#Ensure there are only three y-tick marks
		ax.set_yticks([theta0, (ymax + theta0)/2, ymax])
#We dont want the subplots to bash into each other: tight.layout()
fig.tight_layout()
plt.show()
