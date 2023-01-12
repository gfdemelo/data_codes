#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Plor para explorar a correlação entre taxa de nascimento, expectativa de vida e renda per capita

countries = ['Brazil', 'Madagascar', 'S.Korea', 'United States','Ethiopia', 'Pakistan', 'China', 'Belize']

#Taxa de nascimento para 1000 de população
birth_rate = [16.4, 33.5, 9.5, 14.2, 38.6, 30.2, 13.5, 23.0]
#Expectativa de vida em anos
life_expectancy = [73.7, 64.3, 81.3, 78.8, 63.0, 66.4, 75.2, 73.7]
#Renda por pessoa em dolares em 2000
GDP = np.array([4800, 240, 16700, 37700, 230, 670, 2640, 3490])

fig = plt.figure()
ax = fig.add_subplot(111)
#Cores arbitrárias
colors = range(len(countries))
ax.scatter(birth_rate, life_expectancy, c=colors, s=GDP/10)
ax.set_xlabel('Birth rate per 1000 population')
ax.set_ylabel('Life expectancy at birth (years)')
ax.set_xlim(5,)
ax.set_ylim(60,85)
plt.show() 
