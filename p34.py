#!/usr/bin/python

import time, math

def digit_factorial():
  total_sum = 0
  for n in range(10, 50000):
    partial = 0
    for d in str(n):
      partial += math.factorial(int(d))
    if partial == n:
      total_sum += n
  return total_sum
  
start = time.time()
n = digit_factorial()
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed*1000)