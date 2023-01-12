#!/usr/bin/env python

import numpy as np

def shoelace(n):
	b = np.append(a, a[0]).reshape(len(a)+1,2)
	ib=np.arange(len(b)-1)
	soma1 = np.sum(b[ib,0]*b[ib+1,1])
	soma2 = np.sum(b[ib+1,0]*b[ib,1])
	area = abs(soma1-soma2)*1/2
	print('A área do polígono simples é: ', area, 'cm2') 



a=np.array([[2, 7], [10, 1], [8, 6], [11, 7], [7, 10]])
shoelace(a)
