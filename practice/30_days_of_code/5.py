#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(10):
        print("{x} x {y} = ".format(x=str(n),y=str(i+1))+str((i+1)*n))
    
