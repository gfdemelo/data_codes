#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:16:27 2018

@author: gabriel
"""

x = 23
epsilon = 0.01
increment = epsilon**2
numGuesses = 0
guess = 0.0
while abs(guess**2 -x) >= epsilon and guess <= x:
    guess += increment
    numGuesses += 1
    print ('numGuesses =', numGuesses)
if abs(guess**2 -x) >= epsilon:
    print ('Failed on square root of', x)
else:
    print (guess, 'is close to square root of', x)