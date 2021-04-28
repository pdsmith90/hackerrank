# Enter your code here. Read input from STDIN. Print output to STDOUT



def isPrime(a):    
    if (a <= 1):
        return(False)
    elif (a <= 3):
        return(True)

    #check if divisible by 2 or 3:
    elif (a % 2 == 0 or a % 3 == 0):
        return(False)
    
    #loop
    i = 5
    while(i * i <= a):
        if (a % i == 0 or a % (i + 2) == 0):
            return(False)
        i = i + 6
 
    return(True)
    
    
n=int(input())
for i in range(0,n):
    case=int(input())
    if isPrime(case):
        print("Prime")
    else: print("Not prime")
    
