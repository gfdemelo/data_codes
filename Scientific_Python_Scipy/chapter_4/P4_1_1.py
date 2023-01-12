#!/usr/bin/env python


def average():
	lista=[]
	try:
		arq=open('speed.txt', 'r')	
	except IOError:
		print('Arquivo não pode ser aberto')
	else:
		for line in arq:
			if '#' in line or line.isspace():# or line.endswith('#'):
				continue
			else:
				a=line.strip('\n')
				lista.append(float(a))
	finally:
		print('A média da velocidade é: ', sum(lista)/len(lista))

average()			
