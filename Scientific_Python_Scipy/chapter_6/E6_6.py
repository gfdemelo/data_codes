#!/usr/bin/env python

import numpy as np

#média das alturas
fname = 'eg6-a-student-data.txt'
dtype1 = np.dtype([('genero', '|S1'), ('altura', 'f8')])
a = np.loadtxt(fname, dtype=dtype1, skiprows=9, usecols=(1,3))

m = a['genero'] == b'M'
m_media = a['altura'][m].mean()
f_media = a['altura'][~m].mean()
print('Média de altura masculina: %.2f m, média de altura feminina: %.2f m' % (m_media, f_media))

#média dos pesos, nota-se que há dados faltantes

def parse_weigth(s):
	"""Substitui os valores faltantes por -99"""
	try:
		return float(s)
	except ValueError:
		return -99.
dtype2 = np.dtype([('genero', '|S1'),('peso', 'f8')])
b = np.loadtxt(fname, dtype=dtype2, skiprows=9, usecols=(1,4), converters={4:parse_weigth})
mv = b['peso']>0 #dados válidos
m_pmd = b['peso'][mv & m].mean() #validos e masculinos
f_pmd = b['peso'][mv & ~m].mean() #validos e femininos
print('Média de peso masculina: %.2f kg, média de peso feminina: %.2f kg' % (m_pmd, f_pmd))


#pressão sanguínea
dtype3 = np.dtype([('genero', '|S1'), ('bps', 'f8'), ('bpd', 'f8')])

def reformat_lines(fi):
	for line in fi:
		line = line.replace('/',' ')
		yield line

with open(fname) as fi:
	genero, bps, bpd = np.loadtxt(reformat_lines(fi), dtype3, skiprows=9, usecols=(1,7,8), converters={7: parse_weigth, 8: parse_weigth}, unpack=True)


bps_v = bps > 0 
bpd_v = bpd > 0
m_bps = bps[bps_v & m].mean()
m_bpd = bpd[bpd_v & m].mean()
f_bps = bps[bps_v & ~m].mean()
f_bpd = bpd[bpd_v & ~m].mean()
print('Média de pressão masculina: %.1d-%.1d mm Hg, média de peso feminina: %.1d-%.1d mmHg' % (m_bps, m_bpd, f_bps, f_bpd))



