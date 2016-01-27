import os,sys


inp = raw_input().split()
inp = [int(x) for x in inp]
n = inp[0]
k = inp[1]
#print k

arr = raw_input().split()
arr = [int(x) for x in arr]
oldIndices = sorted(range(len(arr)), key = arr.__getitem__)
newarr = arr[:]
newarr.sort()
#print newarr

totalActivites = 0
totalTime = 0
indices = []
for i in range(len(newarr)):

	if totalTime + newarr[i] <= k:
		totalActivites += 1
		totalTime += newarr[i]
		indices.append(oldIndices[i] + 1)
		#print totalTime

print totalActivites
print ' '.join([str(x) for x in indices])