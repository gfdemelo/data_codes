#!/usr/bin/env python


import pylab

smin,smax=1,30
s=pylab.linspace(smin, smax, 1000)
r=pylab.sqrt(s)
fi=(1+pylab.sqrt(5))/2
theta=2.*pylab.pi*s/fi

for s in range(smax):
	pylab.polar(r, theta)
	r+=pylab.sqrt(s)
pylab.show()
