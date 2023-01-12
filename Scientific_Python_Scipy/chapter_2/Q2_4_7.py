#!/usr/bin/env python


a=('Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
b=(44.7, 65.4, 101.7, 148.3, 170.9, 171.4, 176.7, 186.1, 133.9, 105.4, 59.6, 45.8)

def London(a,b):
	c=zip(b,a)
	lista=[]
	for i in c:
		lista.append(i)
	l=sorted(lista, reverse=True)
	for item in l:
		print(item, end='\n')
London(a,b)
	

