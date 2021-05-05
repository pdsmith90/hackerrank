#!/bin/python3

import math
import os
import random
import re
import sys

firstName=[]
emailID=[]

if __name__ == '__main__':
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName.append(first_multiple_input[0])

        emailID.append(first_multiple_input[1])

        
gmailName=[i[1] for i in list(zip(emailID,firstName)) if re.search(r"\@gmail\.com", i[0])]

print(*sorted(gmailName), sep='\n')
