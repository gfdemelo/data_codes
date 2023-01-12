#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:39:08 2018

@author: gabriel
"""

x = int(input('Qual o número de notas a serem dadas: '))
i=0
res=0


for i in range (0,x):
        y=float(input('Insira uma nota: ' ))
        res = res + y
        i += 1
       
media = res / i
print('A média das notas é: ', media)    
    
    

