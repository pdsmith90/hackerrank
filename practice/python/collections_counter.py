# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
shoeCount = input()
shoes = Counter(list(map(int,input().split())))
N = int(input())
customer=[]
muns=0

for i in range(N):
    customer=list(map(int,input().split()))
    if shoes[customer[0]] > 0:
        shoes[customer[0]] -= 1
        muns+=customer[1]

print(muns)
