#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:12:39 2018

@author: gabriel
"""

s = str(input('Digite algo: '))
x = 0
maior = 0
z = 0


for i in range(len(s)):
     if i != 0:
            if s[i] >= s[i-1]:
                    x += 1
            
            if maior < x:
                    maior = x
                    z = i - x
            else:
                x = 0
                
           
    
print('o maior é: ',s[z:z+maior+1])