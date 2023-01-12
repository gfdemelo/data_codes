#!/usr/bin/env python


import pylab
import random

data=[]
for i in range(5000):
	data.append(random.normalvariate(0,2))
pylab.hist(data, bins=20, normed=True)  #normed = normaliza área das barras a uma unidade
pylab.show()
