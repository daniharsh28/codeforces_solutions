import os,sys

n = int(raw_input())

arr = raw_input().split()
arr = [int(x) for x in arr]

arr.sort()
if arr[0] == 1:
	print -1
else:
	print 1