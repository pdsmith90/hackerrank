#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bigBird=maxBird=0
    arr.sort()
    for i in set(arr):
        currBird=arr.count(i)
        if currBird>maxBird: 
            bigBird=i
            maxBird=currBird
            
    return bigBird
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
