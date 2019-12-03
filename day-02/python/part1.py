#!/usr/bin/env python

""" CHALLENGE:
Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
"""

import sys

OPADD = 1
OPHALT = 99 
OPMULTIPLY = 2

num = [int(i) for i in open(sys.argv[1], "r").read().split(',')]

num[1] = 12
num[2] = 2

for i in range(0, len(num), 4):
    one = num[i + 1]
    two = num[i + 2]
    three = num[i + 3]
    if num[i] == OPADD:
        num[three] = num[one] + num[two]
    elif num[i] == OPMULTIPLY:
        num[three] = num[one] * num[two]
    elif num[i] == OPHALT:
        break
    else:
        print("?")
        
print("Solution: " + str(num[0]))