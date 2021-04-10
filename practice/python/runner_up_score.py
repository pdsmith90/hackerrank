if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    numMax=arr.count(arr[-1])
    del arr[(-1*numMax):]
    print(arr.pop())
