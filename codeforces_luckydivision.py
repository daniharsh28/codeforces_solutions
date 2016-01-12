import os,sys

s = raw_input()

def checkLucky(num):
	flag = False
	for n in num:
		if n in ('4','7'):
			flag = True
		else:
			flag = False
			break
	return flag

def divideLucky(num):
	luckynums = [4,7,44,47,74,77,444,447,474,744,747,777,477,774]
	for anum in luckynums:
		if num % anum == 0:
			return True
	return False


if checkLucky(s) == True or divideLucky(int(s)) == True:
	print 'YES'
else:
	print "NO"
