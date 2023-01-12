#!/usr/bin/env python

import pylab

k1=300 #s-1
k2=100 #s-1
A0=2.0 #mol dm-3

n=1000
tmin,tmax=0,0.02
t=pylab.linspace(tmin, tmax, n)
A=A0*pylab.exp(-(k1+k2)*t)
B=(k1/(k1+k2))*A0*(1-pylab.exp(-(k1+k2)*t))
C=(k2/(k1+k2))*A0*(1-pylab.exp(-(k1+k2)*t))

pylab.plot(t, A, label='[A]')
pylab.plot(t, B, label='[B]')
pylab.plot(t, C, label='[C]')
pylab.xlabel('Time')
pylab.ylabel('[concentration]')
pylab.legend()
pylab.show()
