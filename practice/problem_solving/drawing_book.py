#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n==2 and p==1: return 0
    elif n % 2 == 0 and (p + 1 == n or p+2 ==n): return 1

    else: return min([p // 2, (n-p)// 2])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
