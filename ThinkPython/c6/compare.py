#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:08:37 2020

@author: gabriel
"""

a = int(input('Digite um número para comparação: '))
b = int(input('Digite um número para comparação: '))


def compare(x, y):
        if x > y:
                return 1
        if x == y:
                return 0
        if x < y:
                return -1

compare(2,3)
