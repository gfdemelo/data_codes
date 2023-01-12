#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Emissão de gases de efeito estufa por massa de carbono equivalente

#Emissao anual de gases de efeito estuda, bilhoes de toneladas carbon equivalent (GtCe)
gas_emissions = np.array([(r'$\mathrm{CO_2}$-d', 2.2), (r'$\mathrm{CO_2}$-f', 8.0), ('Nitrous\nOxide', 1.0), ('Methane', 2.3), ('Halocarbons', 0.1)], dtype=[('source', 'U17'), ('emission', 'f4')])

#5 colors
colors = ['#C7B299', '#A67C52', '#C69C6E', '#754C24', '#534741']

explode = [0,0,0.1,0,0]

fig, ax = plt.subplots()
ax.axis('equal') #pizza redondaZZ
ax.pie(gas_emissions['emission'], colors=colors, shadow=True, startangle=90, explode=explode, labels=gas_emissions['source'], autopct='%.1f%%', pctdistance=1.15, labeldistance=1.3)

plt.show()
