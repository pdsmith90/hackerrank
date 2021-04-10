if __name__ == '__main__':
    s = input()
    hasalnum=hasalpha=hasdigit=haslower=hasupper=0
    for ss in s:
        if not hasalnum and ss.isalnum():
            hasalnum = 1        
        if not hasalpha and ss.isalpha():
            hasalpha = 1
        if not hasdigit and ss.isdigit():
            hasdigit = 1
        if not haslower and ss.islower():
            haslower = 1
        if not hasupper and ss.isupper():
            hasupper = 1

    print(str(bool(hasalnum)))    
    print(str(bool(hasalpha)))
    print(str(bool(hasdigit)))
    print(str(bool(haslower)))
    print(str(bool(hasupper)))
