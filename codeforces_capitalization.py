import os,sys

s = raw_input()

out = ''
if s[0].isupper():
	print s
else:
	out += s[0].upper()
	out += s[1:]
	print out
	