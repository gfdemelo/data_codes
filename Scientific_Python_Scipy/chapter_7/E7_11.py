#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Gera uma figura com 10 subplots  apartir da funçao sin(n.np.pi*x), n = 0, 1, ..., 9

nrows=10

fig, axes = plt.subplots(nrows, 1)
#Espaço vertical igual a zero entre os subplots
fig.subplots_adjust(hspace=0)

x = np.linspace(0, 1, 1000)
for i in range(nrows):
	#n-rows para o subplot top, n=0 para o subplot bottom
	n = nrows-i
	axes[i].plot(x, np.sin(n * np.pi * x), 'k', lw=2)
	axes[i].xaxis.set_ticks_position('bottom')
	if i < nrows -1:
		#COloca ticks nos nodos de funcao seno
		axes[i].set_xticks(np.arange(0, 1, 1/n))
		#Labels apenas embaixo do eixo x
		axes[i].set_xticklabels('')
	axes[i].set_yticklabels('')
	
plt.show()
