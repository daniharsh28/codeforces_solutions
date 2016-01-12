import os,sys

n = int(raw_input())

globalMaxCap = 0
maxCap = 0
for i in range(n):
	arr = raw_input().split()
	arr = [int(x) for x in arr]
	a = arr[0]
	b = arr[1]
	maxCap += (b - a)
	if maxCap > globalMaxCap:
		globalMaxCap = maxCap

print globalMaxCap
