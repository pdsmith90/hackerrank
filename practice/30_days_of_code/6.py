# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    rank=str(input())
    print(rank[::2]+' '+rank[1::2])
