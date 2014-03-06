#!/usr/bin/python

import time

def is_pandigital(n, s = 9): 
  n = str(n)
  return len(n) == s and not '1234567890'[:s].strip(n)

def pandigital():
  p = set()
  for i in range(2,100):
    start = 1234
    if i > 9: 
      start = 123
    for j in range(start, 10000/i+1):
      if is_pandigital(str(i) + str(j) + str(i*j)): 
        p.add(i*j)
  return sum(p)

start = time.time()
n = pandigital()
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed*1000)