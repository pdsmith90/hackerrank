#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby


if __name__ == '__main__':
    n = int(input())
    nBin = bin(n)
    nGroup=[]
    nGroup=(list(map(lambda x: [x[0],len(list(x[1]))], groupby(nBin[2:]))))
    nGroup.sort(reverse=True)
    print(nGroup[0][1])
