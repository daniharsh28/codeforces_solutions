import os
import sys

inp = raw_input()
inp = [int(x) for x in inp.split()]

n = inp[0]
k = inp[1]

arr = [int(x) for x in raw_input().split()]

counter = 0
prev = -1
for elem in arr:
    if elem > 0 and counter < k:
        counter += 1
    elif elem > 0 and prev == elem:
        counter += 1
    else:
        break
    prev = elem


print counter
