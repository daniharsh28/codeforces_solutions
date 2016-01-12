import os,sys

n = int(raw_input())
s = raw_input().split()

s = [int(x) for x in s]
s.sort(reverse = True)

sumS = 0
for elem in s:
	sumS += elem

temp = 0
for i in range(len(s)):
	temp += s[i]
	if  temp > (sumS - temp):
		print (i+1)
		break
