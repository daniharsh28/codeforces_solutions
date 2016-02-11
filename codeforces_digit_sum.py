import os,sys
import math

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
m = inp[1]

#Based on the numbers we should decide start and end
start = 1
for i in range(n-1):
	start *= 10

end = 9
multiplier = 0
for i in range(n):
	multiplier += math.pow(10,i)

end = end * multiplier

