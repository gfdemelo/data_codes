#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:47:51 2018

@author: gabriel
"""

def gcd(a,b):
    if b == 0 :
        return a
    return gcd(b,a%b)
            
print (gcd(12,8))