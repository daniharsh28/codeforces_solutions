import os,sys

n = int(raw_input())

arr = raw_input().split()
arr = [long(x) for x in arr]

arr.sort()

result = sum(arr)
auxilarysum = sum(arr)
for i in range(n):
	result += arr[i]
	auxilarysum -= arr[i]
	result += auxilarysum

print result - arr[-1]