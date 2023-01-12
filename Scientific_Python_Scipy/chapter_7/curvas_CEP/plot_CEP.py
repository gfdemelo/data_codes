#!/usr/bin/env python


import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import interp1d

dados = np.genfromtxt('esq', dtype=float, delimiter=None, comments='#')


fig, axes =plt.subplots(nrows=1, ncols=3, figsize=(50,10))
x, y = dados.T[0]*(np.ones(1100).reshape(25,44)), dados.T[1:]
cm = 219474.63

for j in range(3):
	ax = axes[j]
	
	if j==0:
		ax.set_ylabel('Relative Energy (1000 $\mathrm{cm^{-1}}$)')
		for i in range(0,7):
			f = interp1d(x[i], (y[i]-dados.min())*cm/1000, kind='cubic')
			ax.plot(x[i], f(x[i]), lw=1, marker='.', markersize=1.8)

	if j==1:
		for i in range(7,16):
			f = interp1d(x[i], (y[i]-dados.min())*cm/1000, kind='cubic')
			ax.plot(x[i], f(x[i]), marker='.', markersize=1.8)
			ax.set_title('Potential Energy Curves')
			ax.annotate('X $\mathrm{^3 \Sigma^-}$', (5,3))
	if j==2:
		for i in range(16,25):
			f = interp1d(x[i], (y[i]-dados.min())*cm/1000, kind='cubic')
			ax.plot(x[i], f(x[i]), lw=1, marker='.', markersize=1.8)

	ax.set_xlim(3,13)
	ax.set_ylim(-2,40)
	ax.set_xticks(range(3,14,1))
	ax.minorticks_on()
	ax.grid(True, ls='--', lw=.5)			
	ax.text(11,3, '$\mathrm{SI^{+}}$', fontsize=20)
	ax.set_xlabel('Internuclear distance ($\mathrm{a_0}$)')

plt.show()
