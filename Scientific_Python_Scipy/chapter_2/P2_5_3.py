#!/usr/bin/env python3

def Luhn_algorithm(n):
	a=list(str(n))
	b=a[::-1]
	for i in range(1, len(b)):
		if i%2:
			b[i] = str(int(b[i])*2)
			if int(b[i]) > 9:
				c=list(b[i])
				b[i] = str(int(c[0]) + int(c[1]))
	for i in range(len(b)):
		b[i] = int(b[i])				
			
	if not sum(b) % 10:
		return True
	return False 
	
print(Luhn_algorithm(4799273987136272))
		
	
