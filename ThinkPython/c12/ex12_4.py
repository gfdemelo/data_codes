#!/usr/bin/env python3

arq=open('teste.txt')
arq2=open('words.txt')
memo={}
import bisect


def dic(t):
	d=dict()
	for line in t:
		a=line.strip().lower()
		d[a]=None
	return d



def filhos(a, f):
	res=[]
	for i in range(len(a)):
		y=a[:i]+a[i+1:]
		if y in f:
			res.append(y)
	return res

def reducible(t, f):
	if t in memo:
        	return memo[t]
	rs = ['a'] 
	x=filhos(t, f)
	for index in x:
		if reducible(index, f):
			rs.append(index)
	memo[t]=rs
	return rs


def impressao(t):
	if len(t)==0:
		return
	print(t, end='')
	g=reducible(t, arquivo)
	impressao(g[0])



			
def longest(t):
	lista=[]
	for item in t:
		lista.append((len(item), item))
	lista.sort(reverse=True)
	for _, item in lista[0:5]:
		impressao(item)
		print('\n')		
	
arquivo=(dic(arq2))
def todos(t):
	res=[]
	for item in t:
		x=reducible(item, arquivo)
		if x !=[]:
			res.append(item)
	return res

#print(reducible('sprite', arquivo))
#print(todos(arquivo))
longest(todos(arquivo))
	

