#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:58:37 2018

@author: gabriel
"""

x=int(input('Digite um número inteiro x :   '))
y=int(input('Digite outro número inteiro y: '))
z=int(input('E mais um z: '))

if x < y and x < z:
        print('')
        print (x, 'é o menor')
elif y < z:
            print('')
            print (y, 'é o menor')
else:
        print('')
        print (z, 'é o menor')
