import os,sys

string = raw_input()

string = string.lower()

vowels = ('a','e','i','o','u','y')
result = ''
for s in string:
	if s not in vowels:
		result += '.' + s 

print result