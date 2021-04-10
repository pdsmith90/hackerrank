#!/bin/python3

import sys

def lowestTriangle(base, area):
    # iceosoles triange has the least height => a = bh/2 => h = 2a/b
    height = 2 * area / base
    # round to nearest whole integer
    return int(height + (height % 1 > 0))

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
