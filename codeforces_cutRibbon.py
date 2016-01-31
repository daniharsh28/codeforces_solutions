import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
a = inp[1]
b = inp[2]
c = inp[3]

changes = inp[1:]

dp_table = [0 for i in xrange(n+1)]
for ch in changes:
	if ch <= n:
		dp_table[ch] = 1
#if n in changes:
#	print 1
#else:
for i in xrange(n+1):
	for c in changes:
		if c <= i and dp_table[i - c] != 0:
			dp_table[i] = max(1 + dp_table[i - c], dp_table[i])
			#print dp_table
print dp_table[n]
