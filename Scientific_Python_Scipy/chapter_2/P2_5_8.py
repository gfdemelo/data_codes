#!/usr/bin/env python

primos, multiplos=[], []

def Sieve(p):
	for m in range(2,100):
		multiplos.append(p*m)
	number =[n for n in range(p+1,100)]
	for i in range(len(number)):
		if number[i] not in sorted(multiplos):
			primos.append(number[i])
			break
		elif i==len(number)-1:
			return
		else:
			continue
	return Sieve(primos[-1])
Sieve(2)
print(primos)	
