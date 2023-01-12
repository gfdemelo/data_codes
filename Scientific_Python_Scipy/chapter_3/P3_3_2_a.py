#!/usr/bin/env python


import pylab

A=1.024e-23 #J nm^6
B=1.582e-26 #J nm^12
K_b=1.381e-23 #J K-1

rmin,rmax=0.11,1
r=pylab.linspace(rmin, rmax, 1000)
U=(B/(K_b * r**12)) - (A/(K_b * r**6))
line1=pylab.plot(r, U, label='U(r)')
pylab.ylim(-150, 40)
pylab.ylabel('U(r)')
pylab.xlabel('Distância')

pylab.twinx()
F=(12*B/(K_b*r**13)) - (6*A/(K_b*r**7))
line2=pylab.plot(r, F, color='r', label='F(r)')
pylab.ylim(-1000,280)
pylab.ylabel('F(r)')

labels=[]
lines=line1+line2
for line in lines:
	labels.append(line.get_label())


pylab.legend(lines, labels)


pylab.show()




