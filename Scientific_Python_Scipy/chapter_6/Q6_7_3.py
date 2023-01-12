#!/usr/bin/env python


import numpy as np

#Jackpot lottery - 5 números de 1 a 75 e um de 1 a 15 = (n k) = n!/k!*(n=k)! em que n é o número de alternativas e k o de escolhas

print('A Probabilidade de se ganhar na Mega Millions é ', int((np.math.factorial(75)/(np.math.factorial(5)*np.math.factorial(75-5)))*15))

#Impressão de  5 números de 1 a 75 e 1 de 1 a 15

a = (sorted(np.random.choice(np.arange(1,76), 5, replace=False)), np.random.randint(15)+1)
print(a)
