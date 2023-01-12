#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:23:18 2018

@author: gabriel
"""

s = str(input('Digite uma palavra: '))
vogais = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vogais += 1
        
print('Numero de vogais: ',vogais)
