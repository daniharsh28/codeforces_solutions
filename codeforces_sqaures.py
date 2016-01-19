import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

a = inp[0]
b = inp[1]

if a % b == 0:
	print a/b
else:
	counter = 0
	while a > 0 and b > 0:
		if a > b:
			counter += a/b
			a = a % b
		else:
			counter += b/a
			b = b % a

	print counter