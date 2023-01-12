#!/usr/bin/env python


import numpy as np, pylab
from numpy.polynomial import Polynomial


dt=np.dtype([('time', float), ('radius', float)])
dados = np.genfromtxt('new-mexico-blast-data.txt', dtype=dt, skip_header=1)


#Raio(tempo) = constante*Energia^(1/5)*densidade_ar^(-1/5)*t^(-2/5)
#constante ~ 1

tmin, tmax = min(dados['time']/1000), max(dados['time']/1000)
pfit, stats = Polynomial.fit(np.log10(dados['time']/1000), np.log10(dados['radius']),deg=1, full = True, window=(tmin, tmax), domain=(tmin, tmax))

print('Resultados do fit: ', pfit, stats, sep='\n')

lin, coeff = pfit
resid, rank, sing_val, rcond = stats

print('A equação de R(t) é R(t) = %.3f * t^(-2/5) + %.3f \n rms residual = %.4f' % (coeff, lin, np.sqrt(resid[0]/len(dados['radius']))))

density_air = 1.25 #kg m-3
#Energia = (dados['time']**2)*(density_air)*(dados['radius']**5)
Energia = (dados['radius']**5 *density_air)/((dados['time']/1000)**2)
print('A energia liberada é de %.3f J (%.3f kilotons de TNT)' % (Energia.mean(), (Energia/4.184E9).mean()))



pylab.plot(np.log10(dados['time']/1000), np.log10(dados['radius']), 'o',color='r')
pylab.plot(np.log10(dados['time']/1000), pfit(np.log10(dados['time']/1000)), color='k')
pylab.xlabel('log [t] / s')
pylab.ylabel('log R / m')
pylab.show()
