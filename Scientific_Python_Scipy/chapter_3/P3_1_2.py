#!/usr/bin/env python


import math, pylab

V_max=0.1
K_m=0.04


smin,smax=0,1
s=pylab.linspace(smin, smax, 100)
v=(V_max * s)/(K_m + s)

pylab.plot(s,v, label='v x [S]')
pylab.xlabel('[S] / M')
pylab.ylabel('v / M s-1')
pylab.legend(loc='right')
pylab.title('Michaelis-Menten')
pylab.show()

