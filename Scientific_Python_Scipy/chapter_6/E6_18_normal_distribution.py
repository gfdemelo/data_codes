#!/usr/bin/env python


import numpy as np
import pylab

mu, sigma = 100., 8.
samples = np.random.normal(loc=mu, scale=sigma, size=10000)
counts, bins, patches = pylab.hist(samples, bins=100, normed=True)
pylab.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins -mu)**2 / (2*sigma**2)), lw=2)
pylab.show()
