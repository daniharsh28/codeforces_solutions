import os,sys

k = int(raw_input())
l = int(raw_input())
m = int(raw_input())
n = int(raw_input())
d = int(raw_input())

def computeLCM(a,b):

	def computeGCD(a,b):
		while b:
			a, b = b, a%b
		return a

	return (a*b)/computeGCD(a,b)

if (k == 1 or l == 1 or m == 1 or n == 1):
	print d
elif (d < k and d < l and d < m and d < n):
	print 0
else:
	lcmKL = computeLCM(k,l)
	lcmKM = computeLCM(k,m)
	lcmKN = computeLCM(k,n)
	lcmLM = computeLCM(l,m)
	lcmLN = computeLCM(l,n)
	lcmMN = computeLCM(m,n) 

	lcmKLM = computeLCM(lcmKL,m)
	lcmKLN = computeLCM(lcmKL,n)
	lcmLMN = computeLCM(lcmLM,n)
	lcmKMN = computeLCM(lcmKM,n)

	lcmKLMN = computeLCM(lcmKL,lcmMN)

	result = (d/k + d/l + d/m + d/n) - (d/lcmKL + d/lcmKM + d/lcmKN + d/lcmLM + d/lcmLN + d/lcmMN) + (d/lcmKLM + d/lcmKLN + d/lcmLMN + d/lcmKMN) - (d/lcmKLMN)
	print result