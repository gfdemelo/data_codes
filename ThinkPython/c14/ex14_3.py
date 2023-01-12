#!/usr/bin/env python3


import os

def files():
	for root, dirs, files in os.walk('.'):
		lista=[]
		for name in files:
			if name.endswith('.txt'):
				lista.append(os.path.join(root,name))

		for name in dirs:
                	a=os.walk(name)
                	for root, dirs, files in a:
                		for names in files:
                			if names.endswith('.txt'):
                				lista.append(os.path.join(root,names))
		return lista

def duplicados():
	a=files()
	d=dict()
	for name in a:
		cmd='md5sum '+name
		ans=os.popen(cmd)
		res=ans.read()
		nome=res.split()[0]
		if nome not in d:
			d[nome]=name
		else:
			print('Duplicado', d[nome], name)
			
		
		
			
duplicados()

