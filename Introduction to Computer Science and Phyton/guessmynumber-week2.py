#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:41:22 2018

@author: gabriel
"""

print('Please think of a number between 0 and 1000!')

low = 0
high = 1000
ans = (high+low)//2

#guessed=False


while True:    
    print('Is your secret number '+ str(ans) +'?')
    y=input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ' 'c'' to indicate I guessed correctly. ')
    
    if y=='c':
        #guessed = True
        print ('Game over. Your secret number was: '+ str(ans)) 
        break
    elif y=='h':
        high = ans
        ans = (high+low)//2

        
    elif y=='l':
        low = ans
        ans = (high+low)//2

    
     
        
    else:
        print('Sorry, I did not understand your input.')
       
