#!/usr/bin/env python3

arq=open('text.txt')

import string, random, bisect
s=string.punctuation
w=string.whitespace

prefixo=()
sufixo={}

def words(t, ordem=2):	
	for line in t:
		line=line.replace('-', '')
		for word in line.split():
			word=word.replace('"', '')
			word=word.replace('.', '')
			word=word.strip(s+w).lower()
			sufixo(word, ordem)
	
def sufixo(t, ordem=2):
	global prefixo
	if len(prefixo)< ordem:
		prefixo+=(t,)
		print(prefixo)
		return
#	try:
#		sufixo[prefixo].append(t)
#	except KeyError:
	elif  prefixo not in sufixo:
		sufixo[prefixo]=[t]
	
	prefixo=tupla(prefixo, t)


def tupla(t, word):
	return t[1:]+(word,)


def header(t):
	for line in t:
		if line.stratswith('*** END OF THIS'):
        		break



def texto(n):    
	start = random.choice(list(sufixo.keys()))
	for i in range(n):
		suffixes = sufixo.get(start, None)
		if suffixes == None:
			texto(n-i)
			return

		word = random.choice(suffixes)
		print(word, end=' ')
		start = tupla(start, word)

def main(arq, n=100, ordem=2):
	words(arq, ordem)
	texto(n)
	print()

if __name__=='__main__':
	main(arq, 100, 2)
