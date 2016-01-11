import os,sys,math

n = int(raw_input())

arr = raw_input().split()
arr = [int(x) for x in arr]

MAX_TAXI_LIMIT = 4

countTaxi = 0

arrDict = dict()
for elem in arr:
	if elem in arrDict.keys():
		arrDict[elem] += 1
	else:
		arrDict[elem] = 1

print arrDict

