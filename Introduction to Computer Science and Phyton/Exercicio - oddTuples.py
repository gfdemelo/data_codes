#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 18:38:13 2018

@author: gabriel
"""


def oddTuples(aTup):
    oddT = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            oddT = oddT + (aTup[i],)
    return (oddT)
print(oddTuples(aTup))

#outra forma de fazer

#def oddTuples2(aTup):
#return aTup[::2]