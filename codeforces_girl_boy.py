import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
t = inp[1]

queue = raw_input()
arr = []
for q in queue:
	arr.append(q)

while t:
	for i in range(len(arr) - 1):

		if arr[i] == 'B' and arr[i+1] == 'G':
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp
				
				i = i + 2
	t = t-1
print arr