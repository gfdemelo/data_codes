#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:05:15 2018

@author: gabriel
"""
numbers = []

# get user to input 10 integers
for i in range(0, 10):
    numbers.append(int(input("Enter an INT:")))
    
    
# find largest odd number
largest = 0
for number in numbers:
    if number % 2 != 0 and number > largest:
        largest = number
if largest == 0:
    print ("There were no odd integers")
else:
    print (largest)
        
    
