#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Leitura de dados que deem a idade media do primeiro casamento nos eua por 13 decadas desde 1890

year, age_m, age_f = np.loadtxt('eg7-marriage-ages.txt', unpack=True, skiprows=3)
fig = plt.figure()
ax = fig.add_subplot(111)

#Plot de idades de homens e mulheres como marcadores
ax.plot(year, age_m, marker='$\u2642$', markersize=14, c='blue', lw=2, mfc='blue', mec='blue')
ax.plot(year, age_f, marker='$\u2640$', markersize=14, c='magenta', lw=2, mfc='magenta', mec='magenta')
ax.grid(ls='--')

ax.set_xlabel('Year')
ax.set_ylabel('Age')
ax.set_title('Median age at first marriage in the US, 1890-2010')

plt.show()
