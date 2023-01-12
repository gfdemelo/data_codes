#!/usr/bin/env python3


def idade(a):
	i=0
	while i <= 99:
		x=str(i).zfill(2)	
		y=str(a).zfill(2)
		if i <=9:
			if x[:]==y[::-1]:
				print(x, '-', y)
		else:
			if x[:]==y[::-1]:
				print(x, '-', y)
		i=i+1
		a=a+1
					


t=int(input('Digite a diferença de idade: '))


idade(t)	
