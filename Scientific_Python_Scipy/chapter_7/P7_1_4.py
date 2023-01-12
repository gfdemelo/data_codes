#!/usr/bin/env python


import numpy as np, matplotlib.pyplot as plt


dados = np.genfromtxt('co2_mm_mlo.txt', dtype=([('ano', int),('mes', int),('interpolado', float),('trend', float)]),comments='#',delimiter=None, missing_values={-99}, usecols=[0, 1, 4, 5])

#print(dados)

fig = plt.figure()
ax = fig.add_subplot(111)

a = dados['mes']==1
b = dados[a]
lista_year=[b[i][0] for i in range(len(b))]
x = range(len(dados['ano']))

ax.plot(dados['ano'], dados['interpolado'], label='Interpolated')
ax.plot(dados['ano'], dados['trend'], label='Trend')
ax.legend()
ax.set_xticks(lista_year[::2])
ax.tick_params(axis='x', rotation=90)
ax.set_ylabel('$\mathrm{CO_2}$ concentration (ppm)')
#ax.grid(True, ls='--', lw=0.5)
plt.show()

