#!/usr/bin/env python3


def nested_sum(t):
	a=0
	i=0
	while i < len(t):
		b=sum(t[i])
		a=a+b
		i=i+1
	print('A soma dos termos aninhados da lista é : ', a)
	return a



x=[[1,10],[3],[4,5]]

nested_sum(x)
