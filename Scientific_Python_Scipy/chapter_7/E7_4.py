#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

#Plota o decaimento exponencial descrito pot y = Ne^-(t/tau)

#Valor inicial de y em t=0, lifetime in s
N, tau = 10000, 28

#Tempo máximo a ser considerado (s)
tmax = 100
#Grid de pontos e decaimento exponencial
t = np.linspace(0, tmax, 1000)
y = N * np.exp(-t/tau)

fig=plt.figure()
ax = fig.add_subplot(111)
ax.plot(t, y)

#O número de tempos de vida que caem dentro do intervalo do plot
ntau = tmax // tau+1
#xticks em 0, tau, 2*tau, ..., ntau*tau; yticks nos correspondentes valores y
xticks = [i*tau for i in range(ntau)]
yticks = [N * np.exp(-i) for i in range(ntau)]
ax.set_xticks(xticks)
ax.set_yticks(yticks)

#xtick labels: 0, tau, 2tau, ...
xtick_labels = [r'$0$', r'$\tau$'] + [r'${}\tau$'.format(k) for k in range(2, ntau)]
ax.set_xticklabels(xtick_labels)
#ylabels , N, N/e, N/2e
ytick_labels = [r'$N$', r'$N/e$'] + [r'$N/{}e$'.format(k) for k in range (2,ntau)]
ax.set_yticklabels(ytick_labels)

ax.set_xlabel(r'$t\;/\mathrm{s}$')
ax.set_ylabel(r'$y$')
ax.grid()
plt.show()
