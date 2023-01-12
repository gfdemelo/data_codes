#!/usr/bin/env python


import numpy as np


pauli = np.array((
	((0,1), (1,0)),
	((0, -1j), (1j, 0)),
	((1,0), (0,-1))
	))

I2 = np.eye(2)

for sigma in pauli:
	print(np.allclose(sigma.T.conj().dot(sigma), I2))
