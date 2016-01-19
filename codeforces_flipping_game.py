import os,sys

n = int(raw_input())

arr = raw_input().split()
arr = [int(x) for x in arr]

#def count(arr):
#	return arr.count(1)
if arr.count(1) == len(arr):
	print len(arr) - 1
else:
	maxCount = 0
	for i in range(len(arr)):
		for j in range(len(arr)):
			temp = arr[:]
			for counter in range(i,j+1,1):
				temp[counter] = 1 - temp[counter]
			if temp.count(1) > maxCount:
				maxCount = temp.count(1)

	print maxCount
