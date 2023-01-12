#!/usr/bin/env python3

import os

def caminho(t):
	for root, dirs, files in os.walk(t):
		for name in files:
			print(os.path.join(root, name))

caminho('../')
		



