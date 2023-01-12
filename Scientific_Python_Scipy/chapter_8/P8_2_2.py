#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad, dblquad, odeint
import matplotlib.pyplot as plt

#Integral of secant function

interval = np.linspace(-np.pi/2, np.pi/2, 50)
s = np.array([quad(lambda theta: 1/np.cos(theta), 0, item)[0] for item in interval])

#Exact function - inverse of Gudermannian function
gd_inverse = np.array([np.log(abs((1/np.cos(theta)) + np.tan(theta) + 0.00001)) for theta in interval])

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(s[1:-1], interval[1:-1], 'o', label='secante')
ax.plot(gd_inverse[1:-1], interval[1:-1], label='gd$\mathrm{^-1}$')
ax.legend()
plt.show()
