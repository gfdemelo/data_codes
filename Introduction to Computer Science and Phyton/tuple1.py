#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 18:10:22 2018

@author: gabriel
"""

def quociente_e_resto(x, y):
    q = x//y
    r = x%y
    return (q,r)
(quoc, rem) = quociente_e_resto(4,5)
print(quoc, rem)