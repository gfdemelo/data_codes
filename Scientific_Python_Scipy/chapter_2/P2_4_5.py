#!/usr/bin/env python


import random
sequence=['A','G','C','T']
f=''

for i in range(50):
	f+= random.choice(sequence)
print(f)


def DNA(seq,frame):
	if frame==0 or frame==1 or frame==2:
		for i in range(0,len(seq)-3, 3):
			print(seq[frame+i:frame+i++3], end=' ')
		print('\n')
	else:
		print('Frame not valid')
		return

frame = int(input('frame of condons: '))
DNA(f,frame)
