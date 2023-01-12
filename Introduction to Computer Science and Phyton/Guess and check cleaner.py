#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 18:23:28 2018

@author: gabriel
"""

cube = -8

for guess in range(abs(cube+1)):
      if guess**3 >= abs(cube):
          break
if guess**3 != abs(cube):
            print(str(cube) + ' nao e um cubo perfeito') 
else:
    if cube < 0:
           guess = - guess         
    print('Raiz cubica de ', cube, ' é ', guess)