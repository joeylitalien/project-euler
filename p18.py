#!/usr/bin/python

import time

rows = []
f = open("pyramid_p18.txt", "r")
for num in f:
	rows.append([int(i) for i in num.split(" ")])

start = time.time()

for i in reversed(range(len(rows)-1)):
	for j in range(i+1):
		rows[i][j] += max(rows[i+1][j], rows[i+1][j+1])

elapsed = time.time() - start
print "%s found in %s seconds" % (rows[0][0], elapsed)
