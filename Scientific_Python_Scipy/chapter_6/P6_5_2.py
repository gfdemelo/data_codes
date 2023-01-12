#!/usr/bin/env python

import numpy as np

def classify(i):
	A, B, C, D = 'spherical top', 'oblate symmetric top', 'prolate symmetric top', 'asymetric top'
	return A if i[0]==i[1]==i[2] else B if np.isclose(i[0],i[1], atol=1e-6) and i[0]<i[2] else C if i[0]<i[1] and np.isclose(i[1],i[2],atol=1e-6) else D 

def CM(dat):
	massa, x, y, z =dados[:,0], dados[:,1], dados[:,2], dados[:,3]
	massa_total = np.sum(massa)
	x_cm = np.sum(massa*x)/massa_total
	y_cm = np.sum(massa*y)/massa_total
	z_cm = np.sum(massa*z)/massa_total
	A = np.array([x-x_cm, y-y_cm, z-z_cm])
	return A

def rotational_ctes(i):
	h = 6.626e-34 #J.s
	c = 2.9979e8 #m.s-1
	A , B, C = ((h/(8*np.pi**2*c*i[0]))*0.01), (h/(8*np.pi**2*c*i[1]))*0.01, (h/(8*np.pi**2*c*i[2]))*0.01
	print('Ctes rotacionais: A = %.3f cm-1, B = %.3f cm-1, C = %.3f cm-1' %(A, B, C))


if __name__ == '__main__':
	fname='O3.dat','NH3.dat' ,'CH4.dat','CH3Cl.dat'
	for name in fname:
		dados = np.genfromtxt(name, dtype=float, comments='#', delimiter=None)
		massa, x, y, z =dados[:,0], dados[:,1], dados[:,2], dados[:,3]

		coord = CM(dados)*1e-10
		x, y, z = coord[0], coord[1], coord[2]
		I_xx = np.sum(massa*(y**2 + z**2))
		I_yy = np.sum(massa*(x**2 + z**2))
		I_zz = np.sum(massa*(x**2 + y**2))
		I_xy = - np.sum(massa*x*y)
		I_yz = - np.sum(massa*y*z)
		I_xz = - np.sum(massa*x*z)

		I = np.array([[I_xx, I_xy, I_xz],[I_xy, I_yy, I_yz],[I_xz, I_yz, I_zz]])
		I_au = np.sort(np.linalg.eigvals(I))*1.66054e-27

		print(name[:-4],' - ', 'I_a = ', I_au[0],',','I_b = ', I_au[1],',','I_c = ',I_au[2],',', classify(I_au/1e-46))
		rotational_ctes(I_au)
		print('\n')
	

