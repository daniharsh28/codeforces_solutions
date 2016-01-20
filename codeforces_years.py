import os,sys

n = int(raw_input())
while(True):
	cFlag = False
	n = n + 1
	str_n = str(n)
	s = set()
	for ch in str_n:
		if ch in s:
			cFlag = True
		else:
			s.add(ch)

	if(cFlag == True):
		continue
	else:
		print n
		break