#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:48:13 2018

@author: gabriel
"""
import math

def polysum(n,s):
    def area(n,s):
        return (0.25*n*s**2)/math.tan(math.pi/n)
    def perimeter(n,s):
        return n*s
    return round(area(n,s) + perimeter(n,s)**2, 4) 
      
  

    
