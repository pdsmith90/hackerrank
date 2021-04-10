#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum=maximum=scores[0]
    minimumBreak=maximumBreak=0
    for gameScore in scores:
        if gameScore<minimum:
            minimum=gameScore
            minimumBreak+=1
        elif gameScore>maximum:
            maximum=gameScore
            maximumBreak+=1
    return [maximumBreak, minimumBreak]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
