#!/usr/bin/env python

import numpy as np
import pylab as plt

x = np.linspace(0, 1, 20)
y = np.cos(x) + 0.3*np.random.rand(20)
p = np.poly1d(np.polyfit(x, y, 3))
t = np.linspace(0, 1, 200) # use a larger number of points for smoother plotting
plt.plot(x, y, 'o', t, p(t), '-')
plt.show()
