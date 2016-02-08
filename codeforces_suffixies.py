import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
m = inp[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

database = dict()
for i in xrange(len(arr)):
	if arr[i] in database.keys():
		database[arr[i]] += 1
	else:
		database[arr[i]] = 1

#print database

for _ in range(m):
	query_index = int(raw_input())
	
	temp_database = database.copy()
	
	for i in xrange(query_index - 1):
		if temp_database[arr[i]] != 0:
			temp_database[arr[i]] -= 1

	#print database
	print sum([1 for k,v in temp_database.items() if (v > 0)])