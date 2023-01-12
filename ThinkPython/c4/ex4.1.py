#!/usr/bin/env python3

#EXERCÍCIOS DO MEIO DO CAPÍTULO

import turtle
import math

bob=turtle.Turtle()
print(bob)


def square(t, length):
	for i in range(length):
		t.fd(100)
		t.lt(90)


def polygon(t, length, n):
	angle = 360/n
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def circle(t, raio, n):
	circumference=2*math.pi*raio
#	n=50				# uma limitação é que n é uma cte, para calculos 
	length=circumference/n		#mto grandes, as retas sao mto longas e para circulos 
	polygon(t, length, n)		#pequenos perdemos muito tempo. Uma solução seria 
					#tornar n parametro ou ajusta-lo, 
					#n = int(circummference/3)+1

def arc(t, raio, angulo):			#delimita quanto do circulo sera desenhado
	n=50	
	arc_length=2*math.pi*raio*angulo/360
	for i in range(n):
		t.fd(arc_length)
		t.lt(angulo)

arc(bob, 130, 50)
#arc(bob, 30, 130)
#square(bob, 5)
#polygon(bob, 6, 60)
#circle(bob, 42, 150)
#turtle.mainloop()

	
