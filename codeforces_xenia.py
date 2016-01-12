import os,sys

s = raw_input()

x = s.split('+')
x = [int(a) for a in x]


x.sort()
out = str(x[0])
for i in range(1,len(x),1):
	out += '+' + str(x[i])

print out