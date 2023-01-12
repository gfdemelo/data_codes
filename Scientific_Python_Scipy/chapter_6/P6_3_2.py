#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

marks = [45,68,56,23,60,87,75,33,74,59,63,92]
bins = [20,40,60,80,100]

y,x = np.histogram(marks,bins, range=(0,100), density=True)
center = (x[:-1] + x[1:]) / 2
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(10,110)
plt.bar(center,y, width=19,align='center')
plt.show()
