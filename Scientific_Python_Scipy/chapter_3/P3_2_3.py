#!/usr/bin/env python

import pylab

female=[227,5376,10417,4132,2488,1106,421,178,65,21,7]
male=[177,4386,8333,1908,1215,663,279,112,42,15,6]
age=[0,2,10,20,30,40,50,60,70,80,84]


pylab.plot(age, female, label='female')
pylab.plot(age, male, label='male')
pylab.xlabel('Age')
pylab.ylabel('Número de mortes')
pylab.legend()
pylab.show()
