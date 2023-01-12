#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad, dblquad, odeint

#Area of surface revolution

def derivada(x, expoente):
	return x**(expoente-1)*(expoente)


S = 2*np.pi*quad(lambda x: np.sqrt(x)*np.sqrt(1+ (derivada(x, 1/2))**2), 0, 1)[0]
print(S, '-', np.pi*(5**(3/2) - 1)/6)
