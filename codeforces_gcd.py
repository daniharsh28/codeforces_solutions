import os,sys
 
inp = raw_input().split()
inp = [int(x) for x in inp]

a = inp[0]
b = inp[1]
n = inp[2]

def computeGCD(a,b):

	while b:
		a, b = b, a%b
	return a

flag = True
counter = 0
while(flag):
	if (counter % 2 == 0):
		if (n > 0):
			n = n - computeGCD(a, n)
		else:
			print 1
			break
	else:
		if (n > 0):
			n = n - computeGCD(b ,n)
		else:
			print 0
			break
	counter += 1
