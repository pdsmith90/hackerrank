#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalSwaps=0
for i in range(0,n):
    # Track number of elements swapped during a single array traversal
    numberOfSwaps = 0
    
    for j in range(0,n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):            
            a[j + 1], a[j] = a[j], a[j + 1]
            numberOfSwaps+=1
            totalSwaps+=1
    
    
    # If no elements were swapped during a traversal, array is sorted
    if numberOfSwaps == 0:
        break
    
print("Array is sorted in %s swaps." % totalSwaps)
print("First Element: %s" % a[0])
print("Last Element: %s" % a[-1])
