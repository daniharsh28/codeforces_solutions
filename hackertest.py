import os
import sys

n = int(raw_input())


def convert(s):
    if len(s) <= 10:
        return s
    else:
        char1 = s[0]
        char2 = s[len(s) - 1]
        l = len(s) - 2
        return char1 + str(l) + char2

for i in range(n):
    s = raw_input()
    print convert(s)
