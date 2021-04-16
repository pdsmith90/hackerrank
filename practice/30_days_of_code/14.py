#! /usr/bin/env python3

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        
        diffs = [abs(x-y) for x in self.__elements for y in self.__elements]
        
        self.maximumDifference = sorted(diffs).pop()
        
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
