#/usr/bin/env python

import sys
from copy import deepcopy

OPADD = 1
OPHALT = 99 
OPMULTIPLY = 2

def part1():
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
            return "?"
    return num[0]

#=======================
# PART 2
#=======================

def interpret_intcode(noun, verb, num):
    num[1] = noun
    num[2] = verb

    for i in range(0, len(num), 4):
        one = num[i + 1]
        two = num[i + 2]
        three = num[i + 3] 
        if num[i] == OPADD:
            num[three] = num[one] + num[two]
        if num[i] == OPMULTIPLY:
            num[three] = num[one] * num[two]  
        if num[i] == OPHALT:
            break
    return num[0]

def find_value():
    num = [int(i) for i in open(sys.argv[1], "r").read().split(',')]
    for noun in range(0, 100, 1):
        for verb in range(0, 100, 1):
            if interpret_intcode(noun, verb, deepcopy(num)) == 19690720:
                return 100 * noun + verb

print("Part 1: " + str(part1()) + "\n" + "Part 2: " + str(find_value()))