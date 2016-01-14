import os,sys

nums = raw_input()

out = ''
for num in nums:
	temp = int(num)
	if (9 - temp) <= 0:
		out += str(temp)
	else:
		out += str(9-temp)

print out 
