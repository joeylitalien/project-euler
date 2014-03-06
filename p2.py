import math, time

def even_fib(n):
	phi, exp, total = (1 + 5**0.5)/2, 1, 0
	while True:
		fib = round((phi**exp)/(5**0.5))
		if fib >= n:
			break
		if (fib % 2) == 0:
			total += cur
	return total

start = time.time()
n = even_fib(4000)
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed * 1000)
