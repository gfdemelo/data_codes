#!/usr/bin/env python


import math

def double_fatorial(t):
	return 1 if t==0 or t==1 else double_fatorial(t-2)*t
	
print(double_fatorial(6))
					
