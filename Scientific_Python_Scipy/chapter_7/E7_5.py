#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Cria um plot com major, minor ticks customizadas

#Uma seleção de funções em pontos da abcissa rn para 0 <= x < 1
rn = 100
rx = np.linspace(0, 1, rn, endpoint=False)

def tophat(x):
	""" Top har function: y = 1 for x < 0.5, y=0 for x >= 0.5 """
	ry = np.ones(rn)
	ry[rx>=0.5] = 0
	return ry

#Um dicionario de funções escolhidas de
ry = {'half-sawtooth': lambda rx: rx.copy(), 'top-hat':tophat, 'sawtooth':lambda rx: 2* np.abs(rx-0.5)}

#Repete a função escolhida n vezes

nrep = 4
x = np.linspace(0, nrep, nrep*rn, endpoint=False)
y = np.tile(ry['top-hat'](rx), nrep)

fig=plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'k', lw=2)

#Adiciona espaço no fim do plot para melhorar visualização
ax.set_ylim(-0.1, 1.1)
ax.set_xlim(x[0]-0.5, x[-1]+0.5)

#Customiza o tick mark

ax.minorticks_on()
ax.tick_params(which='major', length=10, width=2, direction='inout')
ax.tick_params(which='minor', length=5, width=2, direction='in')
ax.grid(which='both')
plt.show()
