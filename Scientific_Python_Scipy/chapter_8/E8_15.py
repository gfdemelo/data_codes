#!/usr/bin/env python

import numpy as np
from scipy.integrate import tplquad

# The integration limits on x, y, z:
a, b = 0, 1
gfun, hfun = lambda x: 0, lambda x: 1 - x
qfun, rfun = lambda x, y: 0, lambda x, y: 1 - x - y
lims = (a, b, gfun, hfun, qfun, rfun)

# The three different density functions
rhos = [lambda x, y, z: 1,
        lambda x, y, z: x,
        lambda x, y, z: x**2 + y**2 + z**2]

for rho in rhos:
    # The mass as a triple integral of rho over the volume
    m, _ = tplquad(rho, *lims)
    # The centre of mass (xbar, ybar, zbar)
    mxbar, _ = tplquad(lambda x, y, z: x * rho(x,y,z), *lims)
    mybar, _ = tplquad(lambda x, y, z: y * rho(x,y,z), *lims)
    mzbar, _ = tplquad(lambda x, y, z: z * rho(x,y,z), *lims)
    xbar, ybar, zbar = mxbar / m, mybar / m, mzbar / m

    print('mass = {:g}, CofM = ({:g}, {:g}, {:g})'.format(m, xbar, ybar, zbar))
