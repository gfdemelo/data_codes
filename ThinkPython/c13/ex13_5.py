#!/usr/bin/env python3

arq=open('gutemberg.txt')
import random

from ex13_2 import count

def choose_hist(t):
	a=count(t)
	lista=[]
	for item in a:
		lista2=[]
		freq=a[item]
		lista2.append(item)
		lista.extend(lista2*freq)
	print(random.choice(lista))

choose_hist(arq)
