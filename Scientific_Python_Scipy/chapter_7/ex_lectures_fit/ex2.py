#!/usr/bin/env python

import numpy as np
import pylab as plt


x = np.linspace(-1, 1, 2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x, y, 90)
plt.plot(x, y, 'r.')
plt.plot(x, p(x), 'k-', lw=3)
plt.show()
