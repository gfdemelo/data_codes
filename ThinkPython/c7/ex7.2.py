#!/usr/bin/env python3



import math



def eval_loop():
	while True:
		line = input('> ')
		if line == 'done':
			break
		print(eval(line))
	print('Done')

eval_loop()
