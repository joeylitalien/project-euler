#!/usr/bin/python

import math, time

def power_sum(exp, upper):
  total_sum = 0
  for n in range(2, upper):
    partial_sum = 0
    for c in str(n):
      partial_sum += int(c)**exp
    if partial_sum == n:
      total_sum += n
  return total_sum

start = time.time()
n = power_sum(5, 354294)
elapsed = time.time() - start
print "The solution %s was found in %s ms." % (n, elapsed*1000)