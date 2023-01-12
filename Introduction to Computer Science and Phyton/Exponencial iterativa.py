#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 19:03:22 2018

@author: gabriel
"""
base = int(input('Dê um número: '))
exp = int(input('Dê seu expoente: '))

def iterPower(base, exp):
    n =0
    result =1
    while n < exp:
        result = base*result
        n += 1
    return result
    
print(iterPower(base, exp))
#print (iterPower(2, 6))
 
        
