import os,sys

string  = raw_input()

flagFirstUpper = False
flagFoundLower = False

flagFirstUpper = string[0].isupper()


out = string[0].upper()

for i in range(1,len(string),1):
	if (string[i].isupper()):
		out += string[i].lower()
	else:
		flagFoundLower = True
		out += string[i]

if(flagFirstUpper == False and flagFoundLower == True):
	print string
elif(flagFirstUpper == True and flagFoundLower == False):
	print string.lower()
else:
	print out
