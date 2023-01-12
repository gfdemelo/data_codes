#!/usr/bin/env python


import math

gravity=9.81

def range_maximum(velocity,angle):
	global gravity
	return ((velocity**2)*math.sin(2*math.radians(angle)))/gravity

def height_maximum(velocity,angle):
	global gravity
	return ((velocity)*math.sin(math.radians(angle)))**2/(2*gravity)	

v,a=10,30
print('A altura máxima atingida pelo projétil é: ', height_maximum(v,a), 'm')
print('A distância máxima atingida pelo projétil é: ', range_maximum(v,a), 'm')
