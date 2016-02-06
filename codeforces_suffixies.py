import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
m = inp[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

for _ in range(m):
	query_index = int(raw_input())
	counter = 0
	database = set()
	for i in range(query_index-1,len(arr)):
		database.add(arr[i])
	print len(database)