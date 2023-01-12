#!/usr/bin/env python


import numpy as np
from numpy.polynomial import Polynomial

#aceleração do foguete
acc = Polynomial([2.198, 2.842e-2, 1.061e-3])
#print(acc.integ())
print('A distância percorrida é: %.1f m' % (acc.integ().integ()(135.2)))
