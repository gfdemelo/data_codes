#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad

res = quad(lambda x: np.floor(x) - 2*np.floor(x/2), 0, 6)

print('O resultado da integral é: ', res)
