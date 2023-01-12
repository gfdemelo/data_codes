#!/usr/bin/env python


import scipy.constants as pc, scipy.special as sp

def get_wc(d0):
	h = pc.physical_constants['Planck constant'][0]
	c = pc.physical_constants['speed of light in vacuum'][0]
	N_A = pc.physical_constants['Avogadro constant'][0]
	wavelength = h*c*N_A/(d0*10**3)
	print('O comprimento de onda é %.3f nm' %(wavelength*10**9))

get_wc(497)
