#!/usr/bin/env python


import numpy as np
from scipy.special import airy, ai_zeros
import pylab

nmax=16
# Find the first nmax zeros of Ai(x)
a, _, _, _ = ai_zeros(nmax)
# The actual boundary condition is Ai(-qE) = 0 at q=0, so:
qE = -a

def prob_qm(n, dq):
    """
    Return the quantum mechanical probability density for a particle moving
    in a uniform gravitational field.

    """
    # The quantum mechanical wavefunction is proportional to Ai(q-qE) where
    # the qE corresponding to quantum number n is indexed at n-1
    psi, _, _, _ = airy(q-qE[n-1])
    # Return the probability density, after rough-and-ready normalization
    P = psi**2
    return P / (sum(P) * dq)

def prob_cl(n):
    """
    Return the classical probability density for a particle bouncing
    elastically in a uniform gravitational field.

    """
    # The classical probability density is already normalized
    return 0.5/np.sqrt(qE[n-1]*(qE[n-1]-q))

# The ground state, n=1
q, dq = np.linspace(0, 4, 1000, retstep=True)
pylab.plot(q, prob_cl(1), label='Classical')
pylab.plot(q, prob_qm(1, dq), label='Quantum')
pylab.ylim(0,0.8)
pylab.xlabel('q')
pylab.ylabel('P(q)')
pylab.legend()
pylab.show()

# An excited state, n=16
q, dq = np.linspace(0, 20, 1000, retstep=True)
pylab.plot(q, prob_cl(16), label='Classical')
pylab.plot(q, prob_qm(16, dq), label='Quantum')
pylab.ylim(0,0.25)
pylab.xlabel('q')
pylab.ylabel('P(q)')
pylab.legend(loc='upper left')
pylab.show()
