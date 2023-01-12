#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad, dblquad, tplquad


R = 4
r = 1

V = 2*tplquad(lambda z, rho, theta: rho, 0, 2*np.pi, lambda theta: R-r, lambda theta: R+r, lambda  theta, rho: 0, lambda theta, rho: np.sqrt(r**2 - (rho - R)**2))[0]
V_exact = 2*(np.pi)**2 * (R*r**2)
print('V - ', V, V_exact)


I_z = (2/V)*tplquad(lambda z, rho, theta: rho**3, 0, 2*np.pi, lambda theta: R-r, lambda theta: R+r, lambda  theta, rho: 0, lambda theta, rho: np.sqrt(r**2 - (rho - R)**2))[0]
I_z_exact = R**2 + 3/4 *r**2
print('I_z - ', I_z, I_z_exact)

I_x = (2/V)*tplquad(lambda z, rho, theta: (rho**2 * np.sin(theta)**2 + z**2)*rho, 0, 2*np.pi, lambda theta: R-r, lambda theta: R+r, lambda theta, rho: 0, lambda theta, rho: np.sqrt(r**2 - (rho - R)**2))[0]
I_x_exact = 0.5*R**2 + 5/8 * r**2
print('I_x - ', I_x, I_x_exact)
