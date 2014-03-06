#!/usr/bin/python

import time

def spiral(n):
  total_sum = 1
  for i in range(3,n+1,2):
    total_sum += 4*(i**2) - 6*i + 6
  return total_sum


start = time.time()
n = spiral(1001)
elapsed = time.time() - start
print "The answer %s was found in %s ms" % (n, elapsed*1000)