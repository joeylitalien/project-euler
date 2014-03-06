#!/usr/bin/python

def collatz(n):
	counter = 0
	while n > 1:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		counter += 1
	return counter

def longestSeq():
	maxSeq = maxCollatz = 0
	for i in range(1000000):
		if collatz(i) > maxSeq:
			maxSeq = collatz(i)
			maxCollatz = i
	print maxCollatz

longestSeq() 
