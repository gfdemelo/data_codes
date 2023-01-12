#!/usr/bin/env python3

import math

def raiz(a):
    x=a/2
    while True:
        y=(x+a/x)/2
        epsilon=0.000000001
        if abs(y-x) < epsilon:
                return y
        x=y


print('a          raiz(a)            math.sqrt(a)      diff')
print('-          -------            -----------       ----')



def teste_raiz(a):
    while a > 0:
         print(a,'     ', raiz(a),'      ',  math.sqrt(a),'       ', raiz(a)-math.sqrt(a))
         a=a-1





teste_raiz(9)       
