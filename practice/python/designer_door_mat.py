# Enter your code here. Read input from STDIN. Print output to STDOUT 
n,m=map(int,input().split())
repeatSide= [x*2+1 for x in range((n-1)//2)]

#top half
for i in repeatSide:
    print(str(".|."*i).center(m,'-'))

#middle
print("WELCOME".center(m,'-'))

#bottom half
repeatSide.reverse()
for i in repeatSide:
    print(str(".|."*i).center(m,'-'))
