#!/usr/bin/env python

import pylab

#ax=[0,0.5,1,1.5,2,2.5,3]
#ay=[0,0.25,1,2.25,4,6.25,9]

#pylab.plot(ax,ay)
#pylab.show()

import random

ax,ay=[],[]

for i in range(100):
	ax.append(random.random())
	ay.append(random.random())

pylab.scatter(ax,ay)
pylab.show()

