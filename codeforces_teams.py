import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
k = inp[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

arr.sort()

for i in range(0,len(arr),3)

count = n / 3

result = 0
i = 0
while count:
	if arr[i+2] + k <= 5:
		result += 1

	i = i+3
	count -= 1
print result