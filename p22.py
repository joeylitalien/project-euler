#!/usr/bin/python

import time

def getScore(s):
	S = 0
	for c in s:
		S += (ord(c) - 64)
	return S
		
start = time.time()

f = open("names.txt", "r")
names = score = []
names = sorted(f.read().replace('"', '').split(','), key=str)
for i in range(len(names)):
	score.append((i+1)*getScore(names[i]))
total = sum(score)

elapsed = time.time() - start
print "%s found in %s seconds" % (total, elapsed) 
