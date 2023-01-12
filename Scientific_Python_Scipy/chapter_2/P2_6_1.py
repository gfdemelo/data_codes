#!/usr/bin/env python

f=open('redwood.txt', 'r')

def read_file(f):
	diameter,height={},{}
	for line in f:
		if line.startswith('#'):
			continue
		
		a=line.split()
		diameter[a[-2]]=a[0]
		height[a[-1]]=a[0]
	print('A árvore com maior diametro é: ', diameter[max(diameter)])
	print('A árvore com maior altura é: ', height[max(height)])




read_file(f)
