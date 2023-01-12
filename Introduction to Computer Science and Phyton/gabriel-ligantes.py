#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 17:49:51 2018

@author: gabriel
"""
raio = {'N':0.77,'C':0.78,'H':0.37,'O':0.73,'P':1.10}
import math
x = open('exer.xyz', 'r')
a=0
dist_x=[]
dist_y=[]
dist_z=[]
atomos=[]
b = []

for linha in x:
      if linha[0].isalpha():
           valores = linha.split() 
           dist_x.append(float(valores[1]))
           dist_y.append(float(valores[2]))
           dist_z.append(float(valores[3]))
           atomos.append(valores[0])
           a +=1
x.close() 
 
with open('exer.out', 'w') as arq:
    for i in range(0, a):
        for j in range(i + 1, a):
           if i != j:
              distancia = (math.sqrt((dist_x[i] - dist_x[j])**2 + (dist_y[i] - dist_y[j])**2 + (dist_z[i] - dist_z[j])**2))
              ligacao = raio.get(atomos[i]) + raio.get(atomos[j])
              if distancia < ligacao:
                  b.append(("{}{} ----> {}{} - {}".format(atomos[i],i,atomos[j],j,round(distancia, 3))))
    for linha in b:
        arq.write("{}\n".format(linha))            
    
             
     
