#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:07:21 2018

@author: gabriel
"""
#OLD SCRIPT
#x=10000
#ans=0
#iteration=x

#while (iteration !=0):
#    ans = ans + x
#    iteration = iteration - 1
#print (str(x) + 'x' + str(x) + ' = ' + str(ans))    


x = int(input('Digite um número para obter seu quadrado: '))
ans = 0
iteration = 0

while (iteration < x):
	ans = x + ans
	iteration = iteration + 1

print (str(x) + 'x' + str(x) + ' = ' + str(ans)) 
