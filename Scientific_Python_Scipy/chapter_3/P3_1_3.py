#!/usr/bin/env python

import math, pylab

n=100
xmin,xmax=-3,3

x=pylab.linspace(xmin, xmax, n)
desvio=0.5
y=(1/(desvio*pylab.sqrt(2*pylab.pi)))*pylab.exp(-(x**2)/(2*desvio**2))
pylab.ylabel('g(x)')
pylab.xlabel('x')
pylab.title('Gaussian Function')
pylab.plot(x,y, color='magenta', marker='*', linestyle='--')
pylab.show()
