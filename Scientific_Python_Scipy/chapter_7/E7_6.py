#!/usr/bin/env python


import numpy as np, matplotlib.pyplot as plt

#Algunmas espécies de aves perdem peso relativo a area da superfícies de suas asas para maximizar a eficiência aerodinâmica

#Leitura dos dados: dia antes da criação (dar a luz), wing loading (massa corporal por area de asa) e erros para  2 ninhadas

dt = np.dtype([('day', 'i2'),('wl1', 'f8'),('wl1-err','f8'),('wl2','f8'),('wl2-err', 'f8')])

data = np.loadtxt('fledging-data.csv', dtype=dt, delimiter=',')

#Fit-weighted do decaimento exponencial dos dados. Este problema é um problema de mínimos quadrados pois y = Aexp(-Bx) => ln y = ln A - Bx = mx + c

p1_fit = np.poly1d(np.polyfit(data['day'], np.log(data['wl1']), 1, w=np.log(data['wl1'])**-2))

p2_fit = np.poly1d(np.polyfit(data['day'], np.log(data['wl2']), 1, w=np.log(data['wl2'])**-2))

wl1fit = np.exp(p1_fit(data['day']))
wl2fit = np.exp(p2_fit(data['day']))

#Plot dos dados com suas incertezas e fits
fig = plt.figure()
ax = fig.add_subplot(111)

#wl1 data: círculos brancos e black borders, com barras de erros
ax.errorbar(data['day'], data['wl1'], yerr=data['wl1-err'], ls='', marker='o', color='k', mfc='w', mec='k')

ax.plot(data['day'], wl1fit, 'k', lw=1.5)

#wl2 data: círculos pretos, com barras de erros
ax.errorbar(data['day'], data['wl2'], yerr=data['wl2-err'], ls='', marker='o', color='k', mfc='k', mec='k')

ax.plot(data['day'], wl2fit, 'k', lw=1.5)


ax.set_xlim(15,0)
ax.set_ylim(0.003, 0.012)
ax.set_xlabel('days pre-fledging')
ax.set_ylabel('wing loading ($\mathrm{g\, mm^{-2}}$')
plt.show()
