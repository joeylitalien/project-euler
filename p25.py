#!/usr/local/bin/python2.7
 
import time
from math import log10, ceil, sqrt
 
def fibonacci(n):
	phi = (1 + sqrt(5))/2
	f_term = ceil((n-1 + log10(5)/2) / log10(phi))
	return int(f_term)
 
start = time.time()
n = fibonacci(1000)
elapsed = time.time() - start
print "The answer %s was found in %s ms" % (n, elapsed*1000)
