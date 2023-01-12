#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt, matplotlib.image as img, matplotlib.cm as cm


dados = np.load('gb-alt.npy')
a = np.empty((dados.shape))

area_total = np.sum(dados>0)*100
nivel_mar = (0, 10, 50, 100)

fig, axes = plt.subplots(nrows=2, ncols=2)

for i, nivel_mar in enumerate(nivel_mar):
	ax = axes[i//2, i%2]
	area = np.sum(dados>nivel_mar)*100
	copia = dados.copy()
	copia[copia<=nivel_mar] = np.nan
	im = ax.imshow(copia, cmap = cm.Blues_r)
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	percent_area = int(area/area_total)*100
	ax.set_title(('+ %.1d m: %.1d %s' % (nivel_mar, percent_area, '%')), fontsize=11)


cbar = fig.colorbar(ax = [axes[0,1], axes[1,1]], mappable=im, orientation='vertical')
cbar.set_label('Altura acima do mar / m')
plt.show()
