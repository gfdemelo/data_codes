#!/usr/bin/env python

#Cálculo de desvio padrão, média, e histograma para altura de homens e mulheres

import numpy as np
import matplotlib.pyplot as plt

dados_men = np.genfromtxt('ex6-3-f-male-heights.txt', dtype=float)
dados_women = np.genfromtxt('ex6-3-f-female-heights.txt', dtype=float)



print('Cálculo       -    Homem    -  Mulher')
print('Desvio padrão -   %.3f    -  %.3f ' % (np.std(dados_men, ddof=1), np.std(dados_women, ddof=1)))
print('Média         -   %.3f   -  %.3f ' % (np.mean(dados_men), np.mean(dados_women)))

bins=[140,150,160,170,180,190,200]
male_y,male_x = np.histogram(dados_men,bins)
female_y,female_x = np.histogram(dados_women,bins)

center = (male_x[:-1] + male_x[1:]) / 2

p2 = plt.bar(center,female_y, width=9.5,align='center', bottom=male_y, yerr = np.std(dados_women, ddof=1))
p1 = plt.bar(center,male_y, width=9.5,align='center',color='red', yerr=np.std(dados_men, ddof=1))
plt.title('Número de pessoas por sexo e altura')
plt.ylabel('Número de pessoas')
plt.xlabel('Altura')
plt.legend((p1[0], p2[0]), ('Homem', 'Mulher'))
plt.show()

