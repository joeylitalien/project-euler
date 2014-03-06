#!/usr/bin/python

import time

def d(n):
	s = 0
	for i in range(1,n):
		if n%i == 0:
			s += i
	return s

start = time.time()

totalSum = 0
for i in range(1,10000):
	a = d(i)
	b = d(a)
	if i == b and i != a:
		totalSum += i

elapsed = time.time() - start
print "%s found in %s seconds" % (totalSum, elapsed)
