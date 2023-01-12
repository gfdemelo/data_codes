#!/usr/bin/env python

from scipy.integrate import dblquad
import numpy as np

print(dblquad(lambda y, x: 4, 0, 1, lambda x:0, lambda x: np.sqrt(1-(x**2))))
