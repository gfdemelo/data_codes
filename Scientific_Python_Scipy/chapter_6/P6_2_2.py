#!/usr/bin/env python


import numpy as np
import math

fname = 'busiest_airports.txt'
dt = np.dtype([('IATA', 'U3'),('Nome', 'U34'),('location','U40'),('latitude', float),('longitude',float)])
dados = np.genfromtxt(fname, dtype=dt, delimiter='\t')

print(dados)

def distancia(lat1, long1, lat2, long2, raio):
        """ Calcula a distância entre dois pontos em uma esfera de raio R a partir de suas coord1s e coord2s, em que o par em coord é (latitude, longitude)"""

        raiz=np.sqrt(haversine(float(lat2)-float(lat1)) + np.cos(np.radians(float(lat1)))*np.cos(np.radians(float(lat2)))*haversine(float(long2)-float(long1)))
        d = 2*raio*math.asin(raiz)
        return('%d km' % (d))


def haversine(r):
        return (np.sin(np.radians(r)/2))**2

raio=6378.1

aeroporto1 = str(input('Sigla do aeroporto: '))
aeroporto2 = input('Sigla do aeroporto: ')
air1 = dados['IATA']== aeroporto1
air2 = dados['IATA']== aeroporto2
print('A distância entre os aeroportos %s - %s é de %s km' % (dados['Nome'][air1],dados['Nome'][air2],distancia(dados[air1]['latitude'], dados[air1]['longitude'], dados[air2]['latitude'], dados[air2]['longitude'], raio)))


