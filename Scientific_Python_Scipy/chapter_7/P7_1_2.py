#!/usr/bin/env python

import numpy as np, matplotlib.pyplot as plt

year = np.arange(1999, 2009, 1)
neuro_cases = np.array([59, 19,64, 2946, 2866, 1148, 1309, 1495, 1227, 689])
non_neuro_cases = np.array([3, 2, 2, 1210, 6996, 1391, 1691, 2774, 117, 667])

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlabel('Ano')
ax.set_ylabel('Número de casos')
ax.bar(year-0.2, neuro_cases, width=0.4, align='center', label='Neuroinvasive')
ax.bar(year+0.2,non_neuro_cases, width=0.4, align='center', label='non-Neuroinvasive')
ax.set_title('West Nile virus disease in US')
ax.set_xticks(year)
ax.legend()
plt.show()
