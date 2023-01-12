#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 18:36:23 2018

@author: gabriel
"""

def iterPower(base, exp):
    if exp ==0:
        return 1
    if exp ==1:
        return base
    else:
        return base*iterPower(base, exp-1)
    
print (iterPower(2, 5))


