import os,sys

n = int(raw_input())
string = raw_input()

prev = string[0]
count = 0
for i in range(1,len(string)):
	if string[i] == prev:
		count += 1
	prev = string[i]

print count