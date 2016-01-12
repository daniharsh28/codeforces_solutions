import os,sys

s = raw_input()

flag = False
for elem in s:
	if elem in ('H','Q','9'):
		flag = True

if flag == True:
	print "YES"
else:
	print 'NO'