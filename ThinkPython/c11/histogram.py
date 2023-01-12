#!/usr/bin/env python3

#metodo sem get
def histogram(s):
	d=dict()
	for c in s:
		if c not in d:
			d[c]=1
		else:
			d[c]+=1
	return d

#metodo com get



def histograma(s):
	d=dict()
	for c in s:
		d[c]=d.get(c, 0)+1
	return d



print(histograma('banana'))
