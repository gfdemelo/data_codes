#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

dt=np.dtype([('month', int),('year', int),('valor_local', float),('valor_convertido', float)])
dt2=np.dtype([('month', int),('year', int),('valor_local', float)])
dados_arg = np.genfromtxt('argentina-bigmac.txt', dtype=dt, skip_header=1, delimiter=None)
dados_chi = np.genfromtxt('china-bigmac.txt', dtype=dt, skip_header=1, delimiter=None)
dados_uk = np.genfromtxt('uk-bigmac.txt', dtype=dt, skip_header=1, delimiter=None)
dados_us = np.genfromtxt('us-bigmac.txt', dtype=dt2, skip_header=1, delimiter=None)
dados_aus = np.genfromtxt('australia-bigmac.txt', dtype=dt, skip_header=1, delimiter=None)

dados=[(dados_arg,'argentina'), (dados_chi,'china'), (dados_aus, 'australia'), (dados_uk, 'UK')]
fig = plt.figure()
ax = fig.add_subplot(111)
x = range(29)

for item in dados:
	ax.plot(x,(item[0]['valor_convertido']-dados_us['valor_local'])*100/dados_us['valor_local'], label=item[1], marker='.')

ax.set_ylabel('Porcentagem %')
ax.set_title('Porcentagem de diferença do preço do Big Mac em relação ao US')
ax.set_xticks(x)
ax.set_xticklabels((dados_arg['year']))
ax.tick_params(axis='x', rotation=90)
ax.grid(True, ls='--', lw=0.5)
plt.legend()
plt.show()

