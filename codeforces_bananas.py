import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

k = inp[0]
n = inp[1]
w = inp[2]

#Total price needed to buy k bananas
total = 0
for i in range(1,w+1):
	total += i * k

if total - n <= 0:
	print 0
else:
	print total - n