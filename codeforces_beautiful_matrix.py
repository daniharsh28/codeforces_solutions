import os,sys
import math

N = 5
arr = []

def getIndices(arr):
	
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i][j] == 1:
				return i, j 

for i in range(N):
	temp = raw_input().split()
	temp = [int(x) for x in temp]
	arr.append(temp)

row, column = getIndices(arr)
steps = math.fabs(2 - row) + math.fabs(2 - column)
print int(steps)
