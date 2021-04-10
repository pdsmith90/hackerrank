# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import split
from cmath import phase

c=complex(input())
#x,y,j=list(filter(None,split(r"(\W\d+[^+-])",input())))
#y=float(y)
#x=float(x)

r=abs(complex(c))
phi=phase(complex(c))

print(r)
print(phi)
