#!/usr/bin/env python3

import math, copy

class Circle:
	"""REpresenta um círculo
	Atributos: raio(numero), center (objeto Point)"""

class Point:
	"""Representa um ponto no espaço 2D """
	
	def __init__(self, x=10, y=5):		
        	self.x = x
        	self.y = y

	def __str__(self):
		return '%d, %d' % (self.x, self.y)

	def add_point(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def add_tuple(self, other):
		return Point(self.x + other[0], self.y + other[1])


	def __add__(self, other):
		if isinstance(other, Point):
			return self.add_point(other)
		elif isinstance(other, tuple):
			return self.add_tuple(other)
		else:
			raise TypeError('A classe Ponto não sabe como adicionar tipo' + type(other))
		
ponto=Point(1, 2)
ponto2=Point(3,4)

class Rectangle:
	"""Representa um retangulo.
	Atributos: largura, altura e corner"""

def distancia(p1,p2):
	distancia=math.sqrt(abs(p2.x-p1.x)**2+abs(p2.y-p1.y)**2)
	return distancia

def point_in_circle(circ, pto):
	if distancia(circ.center,pto) > circ.raio:
		return False
	else:
		return True

def find_center(rect):
	""" Retorna coordenadas do centro"""

	p=Point()
	p.x=rect.corner.x + rect.width/2
	p.y=rect.corner.y + rect.width/2
	return p

	
def rect_in_circle(circ, rect):
	p=copy.copy(rect.corner)

	if not point_in_circle(circ, p):
		return False            	
	
	p.y+=rect.altura
	if not point_in_circle(circ, p):
		return False 

	p.x += rect.largura	
	if not point_in_circle(circ, p):
		return False 

	p.y -= rect.altura	
	if not point_in_circle(circ, p):
		return False 
	return True

def rect_in_circle_overlap(circ,rect):
	p=copy.copy(rect.corner)

	if distancia(find_center(rect), rect.corner) < circ.raio:
		return True
	else:
		return False
	
def main():
	circulo=Circle()
	circulo.center=Point()
	circulo.center.x=150
	circulo.center.y=100
	circulo.raio=75
	p=Point()
	print(p)
	box=Rectangle()
	box.largura=40.0
	box.altura=30.0
	box.corner=Point()
	box.corner.x=90.0
	box.corner.y=90.0

	

