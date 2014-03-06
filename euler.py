def eratosthenes(limit):
	is_prime = [False]*2 + [True]*(limit - 1) 
	for n in xrange(int(limit**0.5 + 1.5)):
		if is_prime[n]:
			for i in xrange(n*n, limit+1, n):
				s_prime[i] = False
	return [i for i, prime in enumerate(is_prime) if prime]


def gcd(a,b):
	while b:      
		a, b = b, a % b
	return a

def lcm(a,b):
   return (a * b) / gcd(a,b)