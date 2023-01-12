#!/usr/bin/env python

#Calcula a correlação entre numeros menores que 13 na loteria e quantidade de dinheiro ganhada por ganhador

import numpy as np

#dt=np.dtype([('ball1', int),('ball2', int),('ball3', int),('ball4', int),('ball5', int),('ball6', int),('vencedores', int),('dinheiro_por_vencedor', int)])
dados = np.genfromtxt(fname='lottery-draws.txt', dtype=int,  skip_header=2)


amount=[item[-1] for item in dados if item[-1] != 0]
menor_treze=[]

for i in range(len(dados)):
	j=0
	if dados[i,-1]==0:
		continue
	else:
		for item in dados[i]:
			if item <13:
				j+=1
		menor_treze.append(j)

print('A correlação entre números menores que 13 e ganho por pessoa na loteria é: ', abs(np.corrcoef(amount, menor_treze)[0,1]))
				
				 
			 


