#!/usr/bin/env python

element_symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No','Lr','Rf']



def config_electron(n):
	d={'1s':2,'2s':2,'2p':6,'3s':2,'3p':6,'4s':2,'3d':10,'4p':6,'5s':2,'4d':10,'5p':6,'6s':2,'4f':14,'5d':10,'6p':6,'7s':2,'5f':14,'6d':10,'7p':6}

	print(element_symbols[n-1],': ',end='')
	for i in d:
		n=n-d[i]
		if n < 0 or n==0:
			n=d[i]+n	
			print('%s%d' % (i,n))
			print('\n')
			return
		print('%s%d' % (i,d[i]), end='.')


a=input('Número atômico: ')
config_electron(int(a))







