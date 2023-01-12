#!/usr/bin/env python3



import turtle
import math
bob=turtle.Turtle()


def skip(t):
	t.pu()
	t.fd(100)
	t.rt(180)
	t.pd()


def draw_a(t):
	t.lt(70)
	t.fd(100)
	t.rt(130)
	t.fd(100)
	t.lt(180)
	t.fd(50)
	t.lt(60)
	t.fd(40)
	length=100
	skip(t)	

def arc(t, raio, angulo):			#delimita quanto do circulo sera desenhado
	n=31	
	arc_length=2*math.pi*raio*angulo/360
	for i in range(n):
		t.fd(arc_length)
		t.rt(angulo)

def draw_b(t):
	t.lt(90)
	t.fd(170)
	t.lt(-90)
	arc(t, 45, 6)	
	t.rt(180)
	arc(t,45,6)

draw_a(bob)
draw_b(bob)			
