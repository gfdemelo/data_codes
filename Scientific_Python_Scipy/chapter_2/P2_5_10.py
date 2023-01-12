#!/usr/bin/env python

import random
import math

"""One method to estimate the value of π (3.141592...) is by using a Monte Carlo method. In the demo above, we have a circle of radius 0.5, enclosed by a 1 × 1 square. The area of the circle is πr**2=π/4, the area of the square is 1. If we divide the area of the circle, by the area of the square we get π/4.

We then generate a large number of uniformly distributed random points and plot them on the graph. These points can be in any position within the square i.e. between (0,0) and (1,1). If they fall within the circle, they are coloured red, otherwise they are coloured blue. We keep track of the total number of points, and the number of points that are inside the circle. If we divide the number of points within the circle, Ninner by the total number of points, Ntotal, we should get a value that is an approximation of the ratio of the areas we calculated above, π/4.""" 


def pi(n):
	i=0	
	for j in range(n):
		x,y=random.random(),random.random()
		if y < math.sqrt(1-x**2):
			i+=1
	return i
		

n=100000	
print(pi(n))
print('O valor de pi é: ', pi(n)/n*4)

