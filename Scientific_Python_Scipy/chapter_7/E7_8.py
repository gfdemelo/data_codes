#!/usr/bin/env python3.6

import numpy as np, matplotlib.pyplot as plt

#Programa para visualizar a eletricidade produzida  por energia renovável na alemanha de 1990 a 2013

data = np.loadtxt('germany-energy-sources.txt', skiprows=2, dtype='f8')
years = data[:,0]
n = len(years)

#GWh to TWh
data[:,1:] /= 1000

fig = plt.figure()
ax = fig.add_subplot(111)
sources = ('Hidroelétrica', 'Eólica', 'Biomassa', 'Fotovoltaica')
hatch = ['oo', '', 'xxxx', '//']
bottom = np.zeros(n)
bars = [None]*n

for i, source in enumerate(sources):
	bars[i] =ax.bar(years, bottom=bottom, height=data[:,i+1], color='w', hatch=hatch[i], align='center', edgecolor='k')
	bottom += data[:,i+1]

ax.set_xticks(years)
plt.xticks(rotation=90)
ax.set_xlim(1989, 2014)
ax.set_ylabel('Energia Renovável (TWh)')
ax.set_title('Energia renovável na Alemanha, 1990-2013')
plt.legend(bars, sources, loc='best')
plt.show()
