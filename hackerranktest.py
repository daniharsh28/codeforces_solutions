import os
import sys
import math

s = raw_input().split()
s = [int(x) for x in s]

n = s[0]

flag = False
for i in range(2, n, 2):
    if (n - i) % 2 == 0:
        flag = True
        break

if flag == True:
    print 'YES'
else:
    print 'NO'
