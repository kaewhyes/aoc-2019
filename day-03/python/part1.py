#!/usr/bin/env python

import sys

lines = open(sys.argv[1], "r").read().split('\n')

wire1 = lines[0].split(',')
wire2 = lines[1].split(',')

def find_coords(wire):
    x = 0
    y = 0
    coords = []

    for i, move in enumerate(wire):
        units = int(move[1:])
        if move[0] == "R":
            x += units
            for j in range(units):
                coords.append([j, y])
        elif move[0] == "L":
            x -= units
            for k in range(units):
                coords.append([k, y])
        elif move[0] == "U":
            y += units
            for l in range(units):
                coords.append([x, l])
        elif move[0] == "D":
            y -= units
            for m in range(units):
                coords.append([x, m])
        else:
            return -1
    return coords

wire1_coords = find_coords(wire1)
wire2_coords = find_coords(wire2)

print(wire1_coords)
print(wire2_coords)
