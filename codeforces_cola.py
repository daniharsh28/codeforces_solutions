import os,sys

n = long(raw_input())

arr = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

if n <= 5:
	print arr[n-1]
else:
	step = 1L
	size = step * len(arr)
	prev = 0L

	while(size <= n):
		step *= 2
		prev = size
		size += step * len(arr)

	result = (n - prev) / step
	print arr[result]