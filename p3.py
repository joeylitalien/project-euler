#!/usr/bin/python
 
import time
 
def factor(n):
    i, L = 2, [1]
    while i**2 < n:
    	while n % i == 0:
    		n /= i
    		L.append(i)
    	i += 1
    L.append(n)
    return L
 
start = time.time()
n = factor(600851475143)
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed * 1000)