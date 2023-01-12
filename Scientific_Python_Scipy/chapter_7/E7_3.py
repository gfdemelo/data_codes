#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#População de cinco cidades do US

fig = plt.figure()
ax = fig.add_subplot(111)

cities = ['Boston', 'Houston', 'Detroit', 'San Jose', 'Phoenix']
#line styles: solid, dashes, dash-dots and dot-dot-dash
linestyles = [{'ls':'-'},{'ls':'--'},{'ls':':'},{'ls':'-.'},{'dashes':[2,4,2,4,8,4]}]

for i, city in enumerate(cities):
	filename = '{}.tsv'.format(city.lower()).replace(' ','_')
	yr, pop = np.loadtxt(filename, unpack=True)
	line, = ax.plot(yr, pop/1.e6, label=city, c='k', **linestyles[i])

ax.legend(loc='upper left')
ax.set_xlim(1800, 2020)
ax.set_xlabel('Year')
ax.set_ylabel('Population (millions)')
plt.show()
