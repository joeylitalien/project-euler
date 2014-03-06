#!/usr/bin/python

import time

def is_palindrome(word):
    return word == word[::-1]

def palindrome(digit):
	a, p = [], 0
	for i in range((10**digit) - 1, 10**(digit - 1), -1):
		for j in range(i, 10**(digit - 1) + 1, -1):
			if is_palindrome(str(i * j)) and (i * j) > p:
				p = i * j
	return p

start = time.time()
n = palindrome(3)
elapsed = time.time() - start
print "The answer %s was found in %s ms." % (n, elapsed * 1000)
