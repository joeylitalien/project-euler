#!/usr/bin/python

sumOfTheSquares = bigSum = 0

for i in range(101):
	sumOfTheSquares += (i**2)

for j in range(101):
	bigSum += j

print bigSum**2 - sumOfTheSquares
