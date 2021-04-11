#!/bin/python3

import os
import sys
from functools import reduce
#
# Complete the primeCount function below.
#

#sieve of erathosthenes to find prime numbers
#def SieveOfEratosthenes(n):
#    #start with all true array
#    prime = [True for i in range(n+1)]
#    p = 2
#    while (p**2<=n):
#        #starting with p=2, all multiples of p are not primes
#        if (prime[p] == True):
#            for i in range(p**2, n+1, p):
#                prime[i] = False
#        p += 1
#    return list(filter(prime, range(n+1)))


def primeCount(n):
    # the number with the most prime factors will have the smallest primes
    # since 2 is a prime, only have to find primes up to n/2
    
    # hard code first few:
    if n == 1:
        res = 0
    elif n in range(2,6):
        res = 1
        
    else:
        primes=[]
        res=2
        for i in range(2,n//2+1):
            flag=False
            for j in range(2,i-1):
                if i % j == 0:
                    flag=True
                    break
                
            if not flag:
                primes.append(i)
                midwayNum = reduce((lambda x, y: x * y), primes)
                if midwayNum>n:
                    res=len(primes)-1
                    break
                
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
