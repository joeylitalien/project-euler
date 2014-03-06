#!/usr/bin/python

import time
from euler import lcm

start = time.time()
n = reduce(lcm, range(1,21))
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed * 1000)


