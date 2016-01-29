import os,sys

n = int(raw_input())

arr = raw_input().split()
arr = [int(x) for x in arr]

arr.sort()
minElement = arr[0]
maxElement = arr[-1]

minElementOccurences = arr.count(minElement)
maxElementOccurences = arr.count(maxElement)

if (maxElement == minElement):
	print 0, (maxElementOccurences * (maxElementOccurences - 1) / 2)
else:
	print (maxElement-minElement), (minElementOccurences * maxElementOccurences)