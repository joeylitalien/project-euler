#!/usr/bin/python

import time

def powers(lo,hi):
  seq = set()
  for a in range(lo,hi+1):
    for b in range(lo,hi+1):
      seq.add(a**b)
  return len(seq)

start = time.time()
n = powers(2,100)
elapsed = time.time() - start
print "The solution %s was found in %s ms" % (n, elapsed*1000)