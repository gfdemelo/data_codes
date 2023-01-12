#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt, matplotlib.cm as cm

dados=np.genfromtxt('birthday-data.csv', dtype=([('month', int), ('day', int), ('birth', int)]), skip_header=1, delimiter=',')

remover=[i for i in range(len(dados['birth'])) if dados['birth'][i]<1000]
dados=np.delete(dados, remover,0)


heatmap = np.empty((12,31))
heatmap[:] = np.nan

for month, day, birth in dados:
	probabilidade = birth/sum(dados['birth'])*100
	#Indexando os dados. São diminuidos por 1 pois indexacão começa em zero
	heatmap[month-1, day-1] = probabilidade 

#Plot do heatmap

fig=plt.figure()
ax = fig.add_subplot(111)

im = ax.imshow(heatmap, cmap=cm.jet, interpolation='nearest')
ax.set_yticks(range(12))
ax.set_yticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
days = np.array(range(0, 31, 2))
ax.set_xticks(days)
ax.set_xticklabels(['{:d}'.format(day+1) for day in days])
ax.set_xlabel('Day of month')
ax.set_title('Probability of birth per day - 1969-1988')

#Barra de legenda
cbar = fig.colorbar(ax=ax, mappable=im, orientation='horizontal')
cbar.set_label('Probability (%) ')

plt.show()
