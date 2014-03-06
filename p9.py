#!/usr/bin/python

for a in range(1,500):
	for b in range(1,500):
		if (1000*(a+b) == a*b + 500000):
			print a*b*(1000-a-b)
