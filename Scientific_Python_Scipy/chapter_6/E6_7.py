#!/usr/bin/env python


import numpy as np

#Leitura dos dados de stroop.txt e identificação dos valores faltante, substituindo-os por NaN

data = np.genfromtxt('stroop.txt', skip_header=1, dtype=[('estudante', 'u8'),('genero', 'S1'),('black','f8'),('color','f8')], delimiter=',', missing_values='X')
nwords=25

#remove linhas invalidas do conjunto de dados

filtered_data = data[np.isfinite(data['black']) & np.isfinite(data['color'])]

#Extrai linhas por genero e cor (black, color) e normaliza por tempo tomado por cada palavra
fb = filtered_data['black'][filtered_data['genero']==b'F']/nwords
mb = filtered_data['black'][filtered_data['genero']==b'M']/nwords
fc = filtered_data['color'][filtered_data['genero']==b'F']/nwords
mc = filtered_data['color'][filtered_data['genero']==b'M']/nwords


# Produce statistics: mean and standard deviation by gender and word color
mu_fb, sig_fb = np.mean(fb), np.std(fb)
mu_fc, sig_fc = np.mean(fc), np.std(fc)
mu_mb, sig_mb = np.mean(mb), np.std(mb)
mu_mc, sig_mc = np.mean(mc), np.std(mc)
print('Mean and (standard deviation) times per word (sec)')
print('genero | black | color | difference')
print(' F | {:4.3f} ({:4.3f}) | {:4.3f} ({:4.3f}) | {:4.3f}'.format(mu_fb, sig_fb, mu_fc, sig_fc, mu_fc - mu_fb))
print(' M | {:4.3f} ({:4.3f}) | {:4.3f} ({:4.3f}) | {:4.3f}'.format(mu_mb, sig_mb, mu_mc, sig_mc, mu_mc - mu_mb))



