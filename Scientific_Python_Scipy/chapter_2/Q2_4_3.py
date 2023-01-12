#!/usr/bin/env python


def rank(a):
     b=sorted(a, reverse=True)
     for i,c in enumerate(b):
             lista.append(i+1)
     for i in range(len(lista)-1):
             if i==5:
                     return
             if b[i]==b[i+1]:
                     lista[i+1]=lista[i]

a=[87,75,75,50,32,32]
lista=[]
rank(a)
print(lista)
