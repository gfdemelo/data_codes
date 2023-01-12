#!/usr/bin/env python3

import math


class Point():
	"""Representa um ponto no espaço 2D """

def distance_between_points(p1,p2):
	distancia=math.sqrt(abs(p2.x-p1.x)**2+abs(p2.y-p1.y)**2)
	return distancia


def main():
	ponto1=Point()
	ponto2=Point()
	ponto1.x=1
	ponto1.y=1
	ponto2.x=4
	ponto2.y=5
	print(distance_between_points(ponto1,ponto2))

if __name__=='__main__':
	main()
