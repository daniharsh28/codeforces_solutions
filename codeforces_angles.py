import os,sys
import math

n = int(raw_input())

def checkPolygon(angle):

	for i in range(3,361,1):
		if (i-2) * 180 / float(i) == float(angle):
			return 'YES'

	return 'NO'

for i in range(n):

	angle = int(raw_input())

	print checkPolygon(angle)