#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:34:29 2018

@author: gabriel
"""

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
interação = 0


while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    interação += 1
    #print('Interaction number is  ', interação )
print ('Square root of', k, 'is about', guess)
print ('The total number of interactions is equal to ',interação)