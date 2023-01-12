#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:02:18 2018

@author: gabriel
"""
varA = input('digite um numero ou palavra:')
varB = input('digite um numero ou palavra:')


if (type(varA) == str) and (type(varB) == str):
                    print('string involved')
                
if (type(varA) == int) and (type(varB) == int):
                                            if (varA > varB):
                                                            print('bigger')                
                                            if (varA==varB):
                                                            print('equal')
                                            if (varA < varB):
                                                            print('smaller')    
if (type(varA) == str) and (type(varB) == int):
                           print('string involved')
if (type(varA) == int) and (type(varB) == str):
                           print('string involved')