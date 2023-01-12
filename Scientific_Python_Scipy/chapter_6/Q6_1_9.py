#!/usr/bin/env python

#Cria un quadrado mágico. N deve ser impar
#Um quadrado mágico tem uma grade de números N x N na qual a soma de cada linha, coluna e da diagonal é igual a (N(N^2 + 1)/2)

import numpy as np

N = 5
magic_square = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2

while n <= N**2:
        magic_square[i, j] = n
        n += 1
        newi, newj = (i-1) % N, (j+1) % N
        if magic_square[newi, newj]:
                i += 1
        else:
                i, j = newi, newj

print(magic_square)
Nsum = N*(N**2 + 1)/2

print(np.allclose(np.sum(magic_square, axis=0), Nsum))
print(np.allclose(np.sum(magic_square, axis=1), Nsum))
print(np.allclose(np.sum(np.diag(magic_square)), Nsum))
print(np.allclose(np.sum(np.diag(np.fliplr(magic_square))), Nsum))
	
