#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:17:09 2018

@author: gabriel
"""

x=int(input('Digite um número inteiro  :   '))
y=int(input('Digite outro número inteiro : '))
z=int(input('E mais um : '))

if x%2!=0 and y%2!=0 and z%2!=0:
                                if x>y and x>z:
                                    print('o maior número impar é:',x)
                                if z>y and z>x:
                                    print('o maior número impar é:',z)
                                if y>x and y>z:
                                    print('o maior número impar é:',y)

if x%2==0 and y%2!=0 and z%2!=0:
                                if z>y:
                                    print('o maior número impar é:',z)
                                if z<y:
                                    print('o maior número impar é:',y)
                                
if x%2!=0 and y%2==0 and z%2!=0:
                                if x>z:
                                    print('o maior número impar é:',x)
                                if x<z:
                                    print('o maior número impar é:',z)
 
if x%2!=0 and y%2!=0 and z%2==0:
                                if x>y:
                                    print('o maior número impar é:',x)
                                if x<y:
                                    print('o maior número impar é:',y)

if x%2!=0 and y%2==0 and z%2==0:
                                print('o maior número impar é:',x)
                                      
if x%2==0 and y%2!=0 and z%2==0:
                                print('o maior número impar é:',y)

if x%2==0 and y%2==0 and z%2!=0:
                                print('o maior número impar é:',z)                                     
                                      
if x%2==0 and y%2==0 and z%2==0:
        print('Todos os números são pares')                                                            