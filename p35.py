#!/usr/bin/python

import time
import itertools

def eratosthenes(limit):
  is_prime = [False]*2 + [True]*(limit - 1) 
  for n in xrange(int(limit**0.5 + 1.5)):
    if is_prime[n]:
      for i in xrange(n*n, limit+1, n):
        is_prime[i] = False
  return [i for i, prime in enumerate(is_prime) if prime]

def circular_primes(n):
  primes, counter = eratosthenes(n), 0
  for p in primes:
    check = True
    for comb in itertools.combinations(str(p), len(str(p))):
      if comb not in primes:
        check = False
    if check == True: 
      counter += 1
  return counter
  
start = time.time()
p = circular_primes(10000)
elapsed = time.time() - start
print "The answer %s was found in %s ms" % (p, elapsed*1000)
      
