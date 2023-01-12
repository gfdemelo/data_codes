#!/usr/bin/env python3



def sed(s1, s2, arq1, arq2):
	try:
		b=open(arq2, 'w')
		for line in open(arq1):
			a=str(line).replace(s1, s2)
			b.write(a)
		b.close()
	except:
		print('Um erro foi encontrado')	

sed('the', '222', 'text.txt', 'sed_text.txt')
