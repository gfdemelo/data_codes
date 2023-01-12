#!/usr/bin/env python

import numpy as np, math
from scipy.integrate import odeint, quad

g, l = 9.8, 1 #m.s-2, m
theta_inicial = 30
omega = np.sqrt(g/l)
#theta_exact = theta_0*np.cos(omega*t)

theta_0 = theta_inicial

def dthetadt(theta, t):
#	theta1, theta2 = theta
	dtheta1dt = np.sin(math.radians(theta))
	dtheta2dt = -g/l *np.sin(math.radians(theta))
	return dtheta1dt, dtheta2dt

t = np.linspace(0,1, 1)
theta1 = odeint(dthetadt, theta_0, t).T

print(theta1)#, theta2)

