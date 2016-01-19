import os,sys
import math

inp = raw_input().split()
inp = [int(x) for x in inp]

n = inp[0]
m = inp[1]

print int(n + (n-1)/(m-1))