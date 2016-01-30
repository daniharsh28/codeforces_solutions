import os,sys
import math

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
d = inp[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

JOKE_LENGTH = 5

numOfJokes = len(arr) - 1
totalTimeToJoke = numOfJokes * JOKE_LENGTH * 2

result = d - totalTimeToJoke - sum(arr)

if result < 0:
	print -1
else:
	print numOfJokes * 2 + result/5

