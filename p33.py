#!/usr/bin/python

import time

def canceling_frac():
  prod = 1
  for i in range(1,10):
    for j in range(1,i):
      for k in range(1,j):
        ki = k*10 + i
        ij = float(i)*10 + j
        if (k*ij == ki*j):
          prod *= ij/ki
  return int(prod)

start = time.time()
n = canceling_frac()
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed*1000)