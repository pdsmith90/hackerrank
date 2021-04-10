def print_formatted(number):
    # your code goes here
    sp="{:>"+str(len(bin(number)[2:]))+"}"
    
    for i in range(number):
        i+=1
        ii=str(i)
        o=str(oct(i))[2:]
        h=str(hex(i)).upper()[2:]
        b=str(bin(i))[2:]
        
        nums=[sp.format(ii),sp.format(o),sp.format(h),sp.format(b)]
        
        print(' '.join(nums))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
