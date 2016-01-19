import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

m = inp[0]
n = inp[1]

p = None
if m < n:
	p = m
else:
	p = n

if p % 2 == 0:
	print 'Malvika'
else:
	print 'Akshat'
