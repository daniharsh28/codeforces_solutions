import os,sys

inp = raw_input().split()
inp = [int(x) for x in inp]

m = inp[0]
n = inp[1]

arr = []
for i in range(m):
	temp = raw_input()
	temp_list = []
	for t in temp:
		temp_list.append(t)
	arr.append(temp_list)
print arr

rowCounter = m
for i in range(m):
	for j in range(n):
		if arr[i][j] == 'S':
			rowCounter -= 1
			break


columnCounter = n
for j in range(n):
	for i in range(m):
		if arr[i][j] == 'S':
			columnCounter -= 1
			break

print (n * rowCounter + m * columnCounter) - (rowCounter * columnCounter)