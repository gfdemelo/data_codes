#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:39:06 2018

@author: gabriel
"""


def mult(a,b):
    result=0
    while (b> 0):
        result +=a
        b -=1
    return result

print(mult(3,4))