#!/usr/bin/env python

import pylab, math

n=1000
xmin,xmax= -2.*math.pi, 2.*math.pi

x=pylab.linspace(xmin, xmax, n)
y=pylab.sin(x)**2
y1=pylab.sin(x)
y2=pylab.cos(x)**2


pylab.plot(x,y)
pylab.plot(x,y1)
pylab.plot(x,y2)
pylab.show()
