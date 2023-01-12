#!/usr/bin/env python3

P={1,2,3}

def power_set(P):
	yield set(P)
	yield {}
	for item in P:
		a=list(P)
		yield {item}
		a.remove(item)
		yield set(a)
lista=[]
for item in power_set(tuple(P)):
	lista.append(item)


#print(a)
#a=set(lista)
print(sorted(lista, key=len))
