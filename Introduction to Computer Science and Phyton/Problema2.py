#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:43:37 2018

@author: gabriel
"""

s = str(input('Digite: '))
Nbob = 0


for i in range(len(s)):
    if s [i:i+3] == 'bob':# and char=='o' and char=='b':
        Nbob += 1
        
print('Numero de vezes que bob aparece é: ',Nbob)
