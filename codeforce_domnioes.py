import os,sys, math

inp = raw_input().split()

inp = [int(x) for x in inp]

m = inp[0]
n = inp[1]

aread = 2 * 1

result = int(math.floor((m*n)/ float(aread)))
print result