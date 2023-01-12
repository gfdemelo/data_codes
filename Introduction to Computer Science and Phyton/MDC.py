#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:09:57 2018

@author: gabriel
"""

def gdcIter(a,b):
    valorteste = min (a,b)
    while a % valorteste !=0 or b %valorteste != 0:
        valorteste -= 1
    return valorteste
        
print (gdcIter(6,8))        
        
        
                
        
        