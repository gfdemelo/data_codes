#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt, matplotlib.image as mpimg, matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize


def f(x):
	return (4 - 2.1*x[0]**2 + x[0]**4/3)*x[0]**2 + x[0]*x[1] + (4*x[1]**2 - 4)*x[1]**2


x = np.linspace(-2, 2, 1000)
y = np.linspace(-1, 1, 1000)

X, Y = np.meshgrid(x, y)
a = [X,Y]
Z = f(a)

fig = plt.figure()
ax = fig.add_subplot(111)
im=ax.imshow(f([X,Y]), extent=[-2,2,-1,1],cmap=cm.jet)
fig.colorbar(im,orientation='horizontal')


fig2, ax2 = plt.subplots(nrows=1, ncols=1, subplot_kw={'projection':'3d'})
ax2.plot_surface(X, Y, Z, cmap=cm.jet)
fig2.tight_layout()
m = minimize(f, x0=[0,0])
print(m)
ax.scatter(m.x[0], m.x[1], color='k')











plt.show()
