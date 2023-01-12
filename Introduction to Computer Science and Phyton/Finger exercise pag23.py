#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:45:37 2018

@author: gabriel
"""

x = int(input('Enter a postive integer: '))
pwr=0
root=0

for root in range (0,100):
    for pwr in range(0,6):
          if root**pwr == x:
             print(root,pwr)
          
    
    

