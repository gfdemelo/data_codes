#!/usr/bin/env python

import numpy as np
import pylab

fname = 'wb-data.txt'
dados = np.genfromtxt(fname, dtype='U8,U3,U46,U13,(54)i2', delimiter=';',missing_values={'..'}, skip_footer=5, skip_header=1,names=['Pais', 'Pais_code','Nome_serie','Series_code','indicador'])


xmin,xmax = 1960, 2013
x = pylab.linspace(xmin, xmax, 54)

#Thailand
a = dados['Pais'] == 'Thailand'
y = dados[a]['indicador']
pylab.plot(x, y[0], label='BCG')
pylab.plot(x,y[1], label = 'Pol3')
pylab.plot(x,y[2], label =  'Measles')
pylab.title('Thailand')
pylab.legend()
pylab.show()

#Cambodia
a = dados['Pais'] == 'Cambodia'
y = dados[a]['indicador']
pylab.plot(x, y[0], label= 'BCG')
pylab.plot(x,y[1], label = 'Pol3')
pylab.plot(x,y[2], label = 'Measles')
pylab.title('Cambodia')
pylab.legend()
pylab.show()

#Lao PDR
a = dados['Pais'] == 'Lao PDR'
y = dados[a]['indicador']
pylab.plot(x, y[0], label='BCG')
pylab.plot(x,y[1], label = 'Pol3')
pylab.plot(x,y[2], label = 'Measles')
pylab.title('Lao')
pylab.legend()
pylab.show()
