#!/usr/bin/env python


matriz=[[1,2,3],[3,4,5],[6,7,8]]

a=sum(matriz[i][i] for i in range(len(matriz)))
print(a)
