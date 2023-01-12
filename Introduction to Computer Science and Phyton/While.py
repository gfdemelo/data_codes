#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:06:13 2018

@author: gabriel
"""


n = input('Voce esta preso na floresta. Escolha entre ir para a direita ou esquerda: ')

while n == 'direita':
    print('Game Over')
    n = input('Escolha entre ir para a direita ou esquerda: ')

else:
    print('Boa Escolha')