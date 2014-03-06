#!/usr/bin/python

a = []
maxProd = 0

f = open("20x20.txt", 'r')
for m in xrange(20):
	a.append([])
	for n in xrange(20):
		a[m].append(int(f.read(3)))
f.close()

# Check horizontal
for i in range(len(a)):
	for j in range(len(a) - 3):
		horiz = a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3]
		if horiz > maxProd:
			maxProd = horiz

# Check vertical
for i in range(len(a) - 3):
	for j in range(len(a)):
		vert = a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j]
		if vert > maxProd:
			maxProd = vert

# Check left diag
for i in range(3, len(a)):
	for j in range(len(a) - 3):
		lDiag = a[i][j] * a[i-1][j+1] * a[i-2][j+2] * a[i-3][j+3]
		if lDiag > maxProd:
			maxProd = lDiag

# Check right diag
for i in range(len(a) - 3):
	for j in range(len(a) - 3):
		rDiag = a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3]
		if rDiag > maxProd:
			maxProd = rDiag

print maxProd

