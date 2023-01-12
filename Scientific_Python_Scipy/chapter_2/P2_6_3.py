#!/usr/bin/env python

import numpy as np

dt = np.dtype([('name','S8'),('radius',float),('density',float),('vesc',float),('t_sur',float)])
data = np.genfromtxt('ex2-6-g-esi-data.txt', skip_header=3, dtype=dt, comments='--', usecols=(0,2,3,5,7))

dic = {'radius':0.57,'density':1.07,'vesc':0.7,'t_sur':5.58}

for i in range(len(data['name'])):
	prod, j= [], 1
	for item in dic.keys():
		modulo = (data[item][i] - data[item][0])/(data[item][i] + data[item][0])
		prod.append((1 - abs(modulo))**(dic[item]/j))
		j+=1
	print(data['name'][i],  np.product(prod))
