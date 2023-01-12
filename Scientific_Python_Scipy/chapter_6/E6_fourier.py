#!/usr/bin/env python

import numpy as np, pylab

#Função é : f(t) = 2sin(20pi*t) + sin(100pi*t)

#construção do ruído
A1,A2 = 2,1
freq1, freq2 = 10, 50
fsamp = 500
t = np.arange(0, 1, 1/fsamp)
n = len(t)
f = A1*np.sin(2*np.pi*freq1*t) + A2*np.sin(2*np.pi*freq2*t)
f += 0.2 * np.random.randn(n)
pylab.plot(t, f)
pylab.xlabel('Time / s')
pylab.show()

#Transformada de Fourier
F = np.fft.fft(f)
pylab.plot(F.real, 'k', label='reaĺ')
pylab.plot(F.imag, 'red', label='imag')
pylab.legend(loc=2)
pylab.show()

#Espectro de amplitude deslocado para o centro
freq = np.fft.fftfreq(n, 1/fsamp)
F_shifted = np.fft.fftshift(F)
freq_shifted = np.fft.fftshift(freq)
pylab.plot(freq_shifted, np.abs(F_shifted))
pylab.xlabel('Frequency / Hz')
pylab.show()

#Uma vez que a função inpu é real, a transf Fourier é Hermitiana (os componentes de freq negativa são os complexo conjugados da freq positiva)
#Plotando as freq positivas como um espectro de amplitude
spec = 2/n * np.abs(F[:n//2])
pylab.plot(freq[:n//2], spec, 'k')
pylab.xlabel('Frequency Hz')
pylab.show()
