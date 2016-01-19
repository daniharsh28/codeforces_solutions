import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]
n = inp[0]
k = inp[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

arr.sort()

for i in range(0,len(arr),3)