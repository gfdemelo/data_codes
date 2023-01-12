#!/usr/bin/env python

import numpy as np

F = np.matrix([[1, 1],[1,0]])

n=1100

for i in range(1,n+1):
	A = F**i
	print('Fibonacci',i,'=',A[1,1])
	
