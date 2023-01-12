#!/usr/bin/env python

import numpy as np
from scipy.constants import physical_constants

def make_record(k, v):
	""" Retorna o valor da constante a partir da key e value da entrada no dicionário
	physical_constants """

	name = k
	val, units, abs_unc = v
	#Calcula a incerteza relativa em ppm
	rel_unc = abs_unc / abs(val) *1.e6
	return name, val, units, abs_unc, rel_unc

dtype=[('name', 'S50'), ('val', 'f8'), ('units', 'S20'), ('abs_unc', 'f8'), ('rel_unc', 'f8')]

constants = np.array([make_record(k, v) for k,v in physical_constants.items()], dtype=dtype)
constants.sort(order='rel_unc')

#Lista as 10 constantes com maior incertezas relativas

for rec in constants[constants['rel_unc'] > 0][:10]:
	print('{:.0f} ppm: {:s} = {:g} {:s}'.format(rec['rel_unc'], rec['name'].decode(), rec['val'], rec['units'].decode()))
