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
	i = 0
	while(i < len(arr) - 1):
		if arr[i] == 'B' and arr[i+1] == 'G':
			temp = arr[i+1]
			arr[i+1] = arr[i]
			arr[i] = temp

			i = i + 1
		i = i + 1
	t = t - 1

out = ''
for arr_elem in arr:
	out += arr_elem

print out
