#!/usr/bin/python

import math

def triangular():
	incrementer = triangularNum = 0
	flag = True
	while flag:
		incrementer += 1
		triangularNum += incrementer
		if len(getDivisors(triangularNum)) > 500:
			flag = False
	print triangularNum

def getDivisors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

triangular()
