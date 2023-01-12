#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:41:54 2018

@author: gabriel
"""

n = 0

for i in range(5, 11, 2):
    n += i
    if n == 5:
        break
   
print(n)
    