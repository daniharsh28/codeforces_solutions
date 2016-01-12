import os,sys

s = raw_input()

se = set()

for elem in s:
	if elem not in se:
		se.add(elem)

if len(se) % 2 == 1:
	print 'IGNORE HIM!'
else:
	print 'CHAT WITH HER!'