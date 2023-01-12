#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Gráfico de barras para frequencia das letras na língua inglesa.

text_file = 'moby-dick.txt'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Inicializar um dicionario de contagem de letras : {'A':0 ...

lcount = dict([(l,0) for l in letters])

#Leitura do texto e contagem
for l in open(text_file).read():
	try:
		lcount[l.upper()] +=1
	except KeyError:
		#Ignora os caracteres que nao sao letras
		pass


#Numero total de letras
norm = sum(lcount.values())

fig=plt.figure()
ax = fig.add_subplot(111)

#Gráfico barra, com letras na horizontal e freq de letras calculadas como percentagens na altura da barra
x = range(26)
ax.bar(x, [lcount[l]/norm*100 for l in letters], width=0.8, color='g', alpha=0.5, align='center')
ax.set_xticks(x)
ax.set_xticklabels(letters)
ax.tick_params(axis='x', direction='out')
ax.set_xlim(-0.5, 25.5)
ax.yaxis.grid=(True)
ax.set_ylabel('Letter frequency, %')
plt.show()
