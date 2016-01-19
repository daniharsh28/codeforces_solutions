import os,sys

k = int(raw_input())

arr = raw_input().split()
arr = [int(x) for x in arr]

arr.sort(reverse = True)

counter = 0

if sum(arr) < k:
	print -1
else:
	for i in range(len(arr) + 1):
		if counter >= k:
			print i
			break
		else:
			counter += arr[i]

