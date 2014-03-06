#!/usr/bin/python

import time

def make_change(N, L):
  total = [1] + [0]*N
  for coin in L:
    for i in range(coin, N+1):
        total[i] += total[i-coin]
  return total[N]
  
start = time.time()
n = make_change(200, [1,2,5,10,20,50,100,200])
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed*1000)