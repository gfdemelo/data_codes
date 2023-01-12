#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:45:15 2018

@author: gabriel
"""

x = int(input('digite um numero inteiro: '))
if x%2==0:
    if x%3==0:
        print('Divisivel por 2 e 3')
        
    else:
            print('Divisivel por 2 e não por 3')
            
elif x%3 == 0:
        print('Divisivel por 3 e nao por 2')
if x%2!=0 and x%3!=0:
    print('Nao divisivel por 2 e por 3')
