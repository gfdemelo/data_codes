#!/usr/bin/env python

known={0:0, 1:1}
fib=[]

def fibonacci(n):
	if n in known:
		return known[n]
	else:
		return fibonacci(n-1)+fibonacci(n-2)

def dicionario(t):
	d=dict()
	for item in t:
		if item not in d:
			d[item]=1
		else:
			d[item]+=1
	return d

def probabilidade(l,d):
	for item in d:
		print('%.c - %.3f' % (item, d[item]/len(l)))


if __name__=='__main__':
	lista=[]
	for i in range(30):
		fib.append(fibonacci(i))
	for item in fib:
		lista.append(str(item)[0])
	probabilidade(lista,dicionario(lista))

