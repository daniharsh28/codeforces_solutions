import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
m = inp[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

database = set()
count = []
for i in xrange(len(arr)-1,-1,-1):
	database.add(arr[i])
	count.append(len(database))

#print count
#print database

for _ in range(m):
	query_index = int(raw_input())
		
	#print database
	print count[len(arr) - query_index]