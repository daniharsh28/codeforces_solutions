import os,sys

n = long(raw_input())

arr = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

x = 5L
i = 0L
TOTAL = 5
step = 1
for i in range(0L,n,x):
	step = x/TOTAL
	x = 2*x

print step