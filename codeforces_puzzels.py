import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
m = inp[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

arr.sort()
minDifference = 10000000
for i in range(0, m-n + 1,1):
	temp_min = arr[i+n-1] - arr[i]
	if temp_min < minDifference:
		minDifference = temp_min

print minDifference
