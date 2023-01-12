#!/usr/bin/env python


import numpy as np

res=['H', 'T']
tosses = ''.join(res[i] for i in np.random.randint(2, size=10000))

T,H=0,0
T = [T+1 for side in tosses if str(side)==res[1]]
H = [H+1 for side in tosses if str(side)==res[0]]

print('Tails = ', len(T), '\n', 'Heads = ', len(H))
