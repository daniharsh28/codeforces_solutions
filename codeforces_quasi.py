import os,sys

n = int(raw_input())

def isQuasiBinary(number):

	num = str(number)
	for i in xrange(len(num)):
		if num[i] not in ('0','1'):
			return False

	return True

denoms = [j for j in xrange(1,n+1) if isQuasiBinary(j) == True]

dp_table = [k for k in xrange(n+1)]
for denom in denoms:
	dp_table[denom] = 1

result = []
for i in xrange(n+1):
	temp = []
	for denom in denoms:
		if dp_table[i - denom] != 0 and denom <= i:
			dp_table[i] = min(1 + dp_table[i - denom], dp_table[i])
			if min(1 + dp_table[i-denom] , dp_table[i]) == 1 + dp_table[i - denom]:
				temp.append(i - denom)
	result.append(temp)

print dp_table[n]
print result
