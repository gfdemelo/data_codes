#!/usr/bin/env python

import math
import pylab

xmin,xmax = -2.*math.pi, 2.*math.pi

n=1000
x=[0.]*n
y=[0.]*n
dx=(xmax-xmin)/(n-1)

for i in range(n):
	xpt = xmin + i*dx
	x[i] = xpt
	y[i] = math.sin(xpt)**2
	
pylab.plot(x,y)
pylab.show()
