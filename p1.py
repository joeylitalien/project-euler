#!/usr/bin/python

import time

def multiple(a, b, n):
	mul_a = total_a = mul_b = total_b = mul_ab = total_ab = 0
	while mul_a + a < n:
		mul_a += a
		total_a += mul_a
	while mul_b + b < n:
		mul_b += b
		total_b += mul_b
	while mul_ab + (a*b) < n:
		mul_ab += (a*b)
		total_ab += mul_ab
	return total_a + total_b - total_ab

start = time.time()
n = multiple(3, 5, 1000)
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed*1000)
