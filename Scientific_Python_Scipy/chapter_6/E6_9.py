#!/usr/bin/env python


import numpy as np
import pylab

#determina a correlação entre pressão e temperatura dos dados da Cambridge University

data = np.genfromtxt('weather-raw.csv', delimiter=',', usecols=(1,4))

#Remove quaisquer linhas faltando T ou p

data = data[~np.any(np.isnan(data), axis=1)]

#Temperaturas são reportadas por um fator de multiplicação de 10, então removemos esse fator

data[:,0] /= 10

#Coeficiente de correlação
corr = np.corrcoef(data, rowvar=0)[0,1]
print('p-T correlation coefficient: {:.4f}'.format(corr))

#Plot do dado em scatter, T no eixo-x, p no eixo-y
pylab.scatter(*data.T, marker='.')
pylab.xlabel('$T$ /$\mathrm{^\circ C}$')
pylab.ylabel('$p$ /mbar')
pylab.show()
