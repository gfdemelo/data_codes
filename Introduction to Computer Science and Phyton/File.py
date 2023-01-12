#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:01:07 2018

@author: gabriel
"""

namehandle = open ('kids', 'w')

for i in range (3):
    name = input('Enter name: ')
    namehandle.write(name + '\n')
namehandle.close()