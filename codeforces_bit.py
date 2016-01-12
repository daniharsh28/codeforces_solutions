import os,sys

n = int(raw_input())

x= 0
for i in range(n):

	stat = raw_input()
	if (stat == '++X' or stat == 'X++'):
		x += 1
	else:
		x -= 1

print x