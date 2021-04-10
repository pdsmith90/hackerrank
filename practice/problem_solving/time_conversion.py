#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    h,m,sec = map(int, s[:-2].split(':'))
    p=s[-2:]
    if (p.upper()=="PM") & (h!=12): h+=12
    if (p.upper()=="AM") & (h==12): h=00
    return ('%02d:%02d:%02d') % (h,m,sec)
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
