#!/usr/bin/env python

import numpy as np, scipy.constants as pc, pylab
from scipy.optimize import minimize_scalar


T = np.linspace(500, 6000, 1000)

#mi = lambda wavelength: 8*np.pi**2 * pc.physical_constants['Planck constant'] * pc.physical_constants['speed_of_light']/(wavelength**5 * np.exp(pc.physical_constants['Planck constant'] * pc.physical_constants['speed_of_light']/(wavelength * pc.physical_constants['Boltzmann constant']*T)) - 1)


def mi(wavelength, T):
	num =  8*np.pi**2 * pc.physical_constants['Planck constant'][0] * pc.physical_constants['speed of light in vacuum'][0]
	den = wavelength**5 * np.exp(pc.physical_constants['Planck constant'][0] * pc.physical_constants['speed of light in vacuum'][0]/(wavelength * pc.physical_constants['Boltzmann constant'][0]*T)) - 1
	return -num/den

b = minimize_scalar(mi, args=(T))
