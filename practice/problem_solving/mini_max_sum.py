#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    print(str(sum(arr[:(len(arr)-1)]))+' '+str(sum(arr[1:])))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
