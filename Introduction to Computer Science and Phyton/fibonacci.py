#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 18:40:59 2018

@author: gabriel
"""

def  fib(x):
    if x ==0 or x ==1:
        return 1
    else:
        return fib (x-1) + fib (x-2)