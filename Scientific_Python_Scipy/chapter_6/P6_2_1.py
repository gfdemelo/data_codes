#!/usr/bin/env python

import numpy as np
from datetime import datetime, date


def reformat_lines(fi):
	for line in open(fi, 'r'):
		a = line.replace('/','-')
		if ' I' in line:
			a=line.replace(' I', '-I')
		yield a	

def parse_date(s):
	if s.decode('utf-8') == '-':
		return -99
	return s

fname='ex6-2-b-mountain-data.txt'
dt = np.dtype([('Nome', '|U13'),('Altura', 'i4'),('primeira_subida', 'U10'),('primeira_subida_winter', 'U10'),('Location1', 'S10'), ('Location2', 'S10')])
dados = np.loadtxt(reformat_lines(fname), dtype=dt, comments='---',delimiter=None, skiprows=12, converters={3:parse_date})

#O menor pico
m = dados['Altura'].min()
a = dados['Altura']==m
print('O pico de menor altura é o : ', str(dados['Nome'][a]))

#O de mais recente primeira subida
lista=[]
for item in dados['primeira_subida']:
	lista.append(datetime.strptime(item, '%d-%m-%Y'))

conv = max(lista).strftime('%d-%m-%Y').lstrip('0').replace('-0', '-')
c = dados['primeira_subida']==str(conv)
print('O pico com a mais recente primeira subida é: ', dados['Nome'][c])

#O primeiro pico a ser subido no inverno
lista2=[]
for item in dados['primeira_subida_winter']:
	try:
		lista2.append(datetime.strptime(item, '%d-%m-%Y'))
	except ValueError:
		continue

conv = min(lista2).strftime('%d-%m-%Y').lstrip('0').replace('-0', '-')
c = dados['primeira_subida_winter']==str(conv)
print('O pico com primeira subida no inverno é: ', dados['Nome'][c])

#ORdem de montanhas por altura
ordem = np.sort(dados,order='Altura')
print(ordem['Nome'])
