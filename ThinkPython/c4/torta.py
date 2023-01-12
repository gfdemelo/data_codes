#!/usr/bin/env python3


import turtle
import math

bob=turtle.Turtle()


def triangle(t, length, angle):
	t.rt(angle)
	t.fd(length)
	t.lt(90+angle)	
	adj=(length)*(math.sin(angle*math.pi/180))  #trignaulo isosceles tem 2 lados iguais e uma base maior
	t.fd(2*adj)
	t.lt(90+angle)
	t.fd(length)
	t.lt(180-angle)

def pie(t, length, n):
	angle=360/n
	for i in range(n):
		triangle(t, length, angle/2)
		t.lt(angle)

pie(bob, 100, 8)
#triangle(bob,100, 5) 	














#turtle.mainloop()
