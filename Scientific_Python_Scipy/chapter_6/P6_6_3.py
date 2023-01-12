#!/usr/bin/env python


import numpy as np


#Conic Section

A,B,C,D,E,F = 0,0,0,0,0,0

def classify_conic(m):
	m33 = np.array([[m[0,0], m[0,1]], [m[1,0], m[1,1]]])
	if np.linalg.det(m) ==0:
		return 'Two parallel lines' if np.linalg.det(m33)==0 else 'Two intersecting lines' if np.linalg.det(m33) < 0 else 'Single point' if np.linalg.det(m33) > 0 else ValueError
	if np.linalg.det(m) !=0:
		return 'Parabola' if np.linalg.det(m33)==0 else 'Hyperbola' if np.linalg.det(m33) < 0 else 'Circle' if m[0,0]==m[1,1] and m[0,1]==0 and np.linalg.det(m33) > 0 else 'Ellipse' if np.linalg.det(m33) > 0 else ValueError



#A = 1; F = -1
#print(classify_conic(Q)) 
#A = 1/2; D=2; E = -1/2
#print(classify_conic(Q)) 
#A=1/2; C=1/2; D=-2; E=-3; F=2
#print(classify_conic(Q)) 
#A = 9; C=4; F=-36
#print(classify_conic(Q)) 
A = 1; C=1
Q = np.array([[A, B/2, D/2],[B/2, C, E/2], [D/2, E/2, F]])
print(classify_conic(Q)) 

	
	
