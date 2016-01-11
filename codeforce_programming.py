import os,sys

n = int(raw_input())

counter = 0
for i in range(n):
	arr = raw_input().split()
	arr = [int(x) for x in arr]
	if arr.count(1) >= 2:
		counter += 1

print counter
