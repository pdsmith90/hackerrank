def average(array):
    # your code goes here
    arraySet=set(array)
    return(sum(arraySet)/len(arraySet))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
