import os,sys

a = raw_input().lower()
b = raw_input().lower()

sumA = 0L
sumB = 0L
for i in range(len(a)):
	sumA += (len(a) - i) * ord(a[i])
	sumB += (len(a) - i) * ord(b[i])
	if (sumA > sumB):
		print 1
		break
	elif (sumA < sumB):
		print -1
		break
	else:
		continue

if(sumA == sumB):
	print 0