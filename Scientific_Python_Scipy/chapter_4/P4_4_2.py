#!/usr/bin/env python

import sys, math


latitude=sys.argv[1]
longitude=sys.argv[2]

def distancia(coord1, coord2, raio):
	""" Calcula a distância entre dois pontos em uma esfera de raio R a partir de suas coord1s e coord2s, em que o par em coord é (latitude, longitude)"""

	coord1, coord2 = coord1.split(','), coord2.split(',')
	raiz=math.sqrt(haversine(float(coord2[0])-float(coord1[0])) + math.cos(math.radians(float(coord1[0])))*math.cos(math.radians(float(coord2[0])))*haversine(float(coord2[1])-float(coord1[1])))
	d = 2*raio*math.asin(raiz)
	print('%d km' % (d))


def haversine(r):
	return (math.sin(math.radians(r)/2))**2

raio=6378.1
distancia(latitude, longitude, raio)
