#!/usr/bin/env python


import numpy as np, matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = x**3
fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(30,5))

for j in range(4):
	ax = axes[j]
	ax.plot(x, y)
	if j==0:
		ax.set_xscale('log')
		ax.set_ylabel('y')
		ax.set_title('x log scale')
	if j==1:
		ax.set_yscale('log')
		ax.set_title('y log scale')
	if j==2:
		ax.set_xscale('log')	
		ax.set_yscale('log')
		ax.set_title('x and y in log scale')
	if j==3:
		ax.set_xscale('symlog')
		ax.set_title('x in symlog')
	ax.set_xlabel('x')
	
plt.show()	 
