#!/usr/bin/python

import time

def latticePath(n):
	L = [1] * n
	for i in range(n):
		for j in range(i):
			L[j] += L[j-1]
		L[i] = 2 * L[i-1]
	return L[n-1]

start = time.time()
n = latticePath(1000)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n, elapsed)
