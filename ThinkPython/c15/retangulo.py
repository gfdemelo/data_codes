#!/usr/bin/env python3

import math, copy


class Point():
	"""Representa um ponto no espaço 2D """


class Rectangle:
	"""Representa um retangulo.
	Atributos: largura, altura e corner"""

def find_center(rect):
	""" Retorna coordenadas do centro"""

	p=Point()
	p.x=rect.corner.x + rect.width/2
	p.y=rect.corner.y + rect.width/2
	return p


def print_point(p):
	"""Imprime o ponto de maneira legível, sem ele não conseguimos ler"""
	print('(%g, %g)' % (p.x,p.y))

def move_rectangle(rect, dx, dy):
	novo=copy.deepcopy(rect)
	novo.corner.x += dx
	novo.corner.y +=dy
	return novo

def main():
	box=Rectangle()
	box.width=100.0
	box.height=200.0
	box.corner=Point()
	box.corner.x=0.0
	box.corner.y=0.0
	a=move_rectangle(box,50,50)	
	center=find_center(a)
	print_point(center)


main()
