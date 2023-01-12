#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Plot of the Planck Function

T = 5778 #K
# Physical constants in SI units: Planck's constant (J.s),
# the speed of light (m.s-1), Boltzmann's constant (J.K-1)
h, c, kB = 6.62606957e-34, 299792458, 1.3806488e-23

wavelength_min, wavelength_max = 100*1.e-9, 5000*1.e-9 #nm
wavelength = np.linspace(wavelength_min, wavelength_max, 1000)

intensity=(2*h*c**2)/((wavelength**5)*(np.exp((h*c)/(wavelength*kB*T))-1))


fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(wavelength*1.e-9,intensity, c='r')
ax.set_xlabel('wavelength (nm)')
ax.set_ylabel('Intensity')
ax.set_title('Planck function for the sun (T = 5778 K)')
plt.show()
