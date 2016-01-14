import os,sys

n = int(raw_input())
counter = 0
for i in range(n):
	inp = raw_input().split()
	inp = [int(x) for x in inp]
	p = inp[0]
	q = inp[1]

	if (q-p >= 2):
		counter += 1

print counter
