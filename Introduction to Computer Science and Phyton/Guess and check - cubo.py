#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:56:01 2018

@author: gabriel
"""

x = int(input('Digite um número: '))
ans = 0

while ans**3 < x:
    ans = ans + 1
if ans**3!= x :
    print(str(x) + ' nao e um cubo inteiro')
else:
    print ('a raiz cubica de ' + str(x) + ' is ' + str(ans))    