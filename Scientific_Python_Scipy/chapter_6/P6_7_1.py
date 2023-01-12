#!/usr/bin/env python

import numpy as np
import pylab

#A experiment is carried out ntrials times in which n coins are tossed and the total number of heads each time is recorded

ntrials = 100
n = 100 #  number of coins tossed
a = np.random.randint(2, size=(ntrials, n))
Heads=np.array([np.sum(side==0) for side in a])

_, bins, _ = pylab.hist(Heads, bins=ntrials-1, normed=True, histtype='bar')
#Binomial distribution
b =[np.math.factorial(ntrials)/(np.math.factorial(int(item))*np.math.factorial(ntrials - int(item))) for item in bins]
c = b*0.5**(bins) * (1-0.5)**(ntrials-bins)
print(c)
pylab.plot(bins, c)

#Distribuição normal
pylab.plot(bins,1/(Heads.std() * np.sqrt(2*np.pi))*np.exp(-(bins - Heads.mean())**2 / (2*Heads.std()**2)), lw=2) 
pylab.xlabel('Number of Heads')
pylab.ylabel('Probability')
pylab.show()
