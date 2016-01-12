import os,sys

arr = raw_input()

currZero = 0
currOne = 0
flagOne = False
flagZero = False
for a in arr:
	if (a == '1'):
		currOne += 1
		currZero = 0
		if (currOne >= 7):
			flagOne = True
	else:
		currZero += 1
		currOne = 0
		if (currZero >= 7):
			flagZero = True


if (flagOne == True or flagZero == True):
	print 'YES'
else:
	print 'NO'