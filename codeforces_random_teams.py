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

	minInCluster = n / m 
	entriesInCluster = [n/m for _ in xrange(m)]

	for i in xrange(n % m):
		entriesInCluster[i] += 1

	totalMin = 0
	for entry in entriesInCluster:
		if entry >= 2:
			totalMin += entry * (entry - 1) / 2


	maxiInOneCluster = n - (m-1)

	print totalMin , maxiInOneCluster * (maxiInOneCluster - 1)/2




