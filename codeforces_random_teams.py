import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
m = inp[1]

if m == 1:
	maxiInOneCluster = minInOneCluster = n * (n-1) / 2
	print minInOneCluster, maxiInOneCluster
elif m == n:
	print 0, (m - n) * (m - n - 1)/2
else:

	numOfEntriesInCluster = n / m 
	
	numOfEntriesWithModulus =  n % m 
	numOfEntriesWithoutModulus = m - numOfEntriesWithModulus

	totalMin = 0
	if numOfEntriesInCluster >=2 :
		totalMin +=  numOfEntriesWithoutModulus * numOfEntriesInCluster * (numOfEntriesInCluster-1) / 2
		
	totalMin += numOfEntriesWithModulus * (numOfEntriesInCluster) * (numOfEntriesInCluster + 1) / 2

	maxiInOneCluster = n - (m-1)

	print totalMin , maxiInOneCluster * (maxiInOneCluster - 1)/2