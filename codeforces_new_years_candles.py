import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

a = inp[0]
b = inp[1]

counter = 0
counter += a

while a:
	remainder = a%b
	a = a/b
	counter += a
	a += remainder

	if a < b:
		break

print counter