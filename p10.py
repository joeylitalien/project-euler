#!/usr/bin/python

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in xrange(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in xrange(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

print sum(primes_upto(2000000))
