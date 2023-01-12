#!/usr/bin/env python


import pylab

a=0.8
b=2
theta_min,theta_max=0,8.*pylab.pi
theta=pylab.linspace(theta_min, theta_max, 10000)
r=a**theta
pylab.polar(theta,r, color='red')
pylab.show()
