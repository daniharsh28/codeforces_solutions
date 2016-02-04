import os,sys

inp = raw_input()

arr = [0]
for i in range(1,len(inp)):
	if inp[i] == inp[i-1]:
		arr.append(arr[-1] + 1)
	else:
		arr.append(arr[-1])

print arr
m = int(raw_input())
for _ in range(m):
	query = raw_input().split()
	query = [int(x) for x in query]

	p = query[0]
	q = query[1]
	print arr[q-1] - arr[p-1]