#!/usr/bin/python

import time, euler

def truncable_primes():
	primes = eratosthenes(1000000)
	count = s = 0
	for p in primes:
		for exp in range(len(str(p))):
			if divmod(p, 10**exp) in primes:
				



start = time.time()
n = truncable_primes()
elapsed = time.time() - start
print "The answer %s was found in %s ms" % (n, elapsed * 1000)