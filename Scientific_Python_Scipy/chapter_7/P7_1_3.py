#!/usr/bin/env python


import numpy as np, matplotlib.pyplot as plt

dt=np.dtype([('country', 'S10'), ('dados', float)])
gdp = np.genfromtxt('gdp.tsv', dtype=dt, delimiter='\t', filling_values={1:-999.})
bmi = np.genfromtxt('bmi_men.tsv', dtype=dt, delimiter='\t', filling_values={1:-999.})
population = np.genfromtxt('population_total.tsv', dtype=dt, delimiter='\t', filling_values={1:-999.})

fig = plt.figure()
ax = fig.add_subplot(111)


def removing_data(data):
	lista=[i for i in range(len(data)) if data[i][1]==-999.]
	data2 = np.delete(data, lista, axis=0)
	lista2=[item[0] for item in data2 for i in range(len(bmi)) if item[0]==bmi[i][0]]
	lista3=[i for i in range(len(data2)) if data2[i][0] not in lista2]
	data3=np.delete(data2, lista3, 0)
	return data3


population_2  = removing_data(population)
gdp_2 = removing_data(gdp)


colors=range(199)#len(bmi))
print(len(bmi), len(gdp_2), len(population_2))
ax.scatter(gdp_2['dados'], bmi['dados'], s=population_2['dados']/10**9 *2000, c=colors, edgecolor='w')
ax.set_alpha(0.75)
ax.set_xlabel('GDP per capita')
ax.set_ylabel('BMI men')
ax.set_xlim(10**2,10**5)
ax.set_ylim(18, 36)
ax.set_xscale('log')
plt.show()
