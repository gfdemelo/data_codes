#!/usr/bin/env python3

arq=open('words.txt')

def count_words(t):
	for line in arq:
		count=0
		t=line.strip()
		for letter in line:
			count=count+1
			if count > 20:
				print(line)

count_words(arq)

#outra opção
with open('words.txt') as f: 
    b=[] 
    a=f.readlines() 
    for item in a: 
        b.append(item.rstrip('\n')) 
    lista=[item for item in b if len(item)>20] 

