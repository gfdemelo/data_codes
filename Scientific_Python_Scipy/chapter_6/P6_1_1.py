#!/usr/bin/env python


import numpy as np

dt = np.dtype([('Name', 'S4'),('Population', int),('Mass/tones',float)])
a = np.array([('Bowhead', 9000, 60),('Blue whale',20000, 120),('Fin whale', 100000, 70),('Humpback whale', 80000, 30), ('Gray whale', 26000, 35),('Atlantic white-sided', 250000, 0.235),('Pacific white-sided',1000000, 0.15),('Killer whale', 100000, 4.5),('Narwhal', 25000, 1.5),('Beluga', 100000, 1.5),('Sperm whale', 2000000, 50),('Baiji', 13, 0.13),('North Atlantic', 300, 75),('North Pacific', 200, 80),('Southern right', 7000, 70)], dtype=dt)

a.sort(order = 'Population')
print(a)
c = np.array([('Brydes whale',100000, 25)], dtype=dt)
print(np.searchsorted(a['Population'], c['Population']))
 
