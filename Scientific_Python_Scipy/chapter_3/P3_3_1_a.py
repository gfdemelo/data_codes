#!/usr/bin/env python


import pylab

a=0
b=2
theta_min,theta_max=0,8.*pylab.pi
theta=pylab.linspace(theta_min, theta_max, 1000)
r=a+b*theta
pylab.polar(theta,r, color='red')
pylab.show()
