#!/bin/python3

import os
import sys

#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):
    # number of pairs of grid squares plus remainders
    nn = int(n // 2 + (n % 2 > 0))
    mm = int(m // 2 + (m % 2 > 0))
    return nn * mm
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
