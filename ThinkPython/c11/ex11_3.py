#!/usr/bin/env python3


ack={}


def ackermann(m, n):
	if (m,n) in ack:
		return ack[m,n]
	elif m == 0:
		ack[m,n]=n + 1
		return n+1
	elif m > 0 and n == 0:
		ack[m,n]=ackermann(m-1, 1)
		return ackermann(m-1, 1)
	else:
		ack[m,n]=ackermann(m-1, ackermann(m, n-1))
		return ackermann(m-1, ackermann(m, n-1))

	
print(ackermann(3,4))
print(ack)
