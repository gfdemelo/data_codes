#!/usr/bin/env python

import scipy.constants as pc

Density = pc.atm/(pc.physical_constants['Boltzmann constant'][0]*pc.zero_Celsius)

print('A densidade molar N/V é %.3e partículas/m^3' % (Density))
