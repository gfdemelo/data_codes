#!/usr/bin/env python

import pylab, math

n=1000
xmin,xmax=-20,20

x=pylab.linspace(xmin, xmax, n)
y=pylab.log(1/pylab.cos(x)**2)
y1=pylab.log(1/(pylab.sin(x)**2))

pylab.plot(x,y)
pylab.plot(x,y1)
pylab.show()
