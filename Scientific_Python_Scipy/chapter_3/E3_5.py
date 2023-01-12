#!/usr/bin/env python

import pylab

theta=pylab.linspace(0, 1.*pylab.pi, 1000)
a=1
#r=2*a*(1. + pylab.cos(theta))
r=pylab.cos(theta)
pylab.polar(theta,r)
pylab.show()
