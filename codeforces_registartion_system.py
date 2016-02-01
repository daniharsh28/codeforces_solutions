import os,sys

n = int(raw_input())

database = dict()

for _ in range(n):

	temp_str = raw_input()
	if (temp_str not in database):
		print 'OK'
		database[temp_str] = 1
	else:
		print temp_str + str(database[temp_str])
		database[temp_str] += 1
