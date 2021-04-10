def functionn(x,y,z,n):
    for i in range(x+1): 
        for j in range(y+1): 
            for k in range(z+1): 
                if i+j+k != n: listijk.append([i,j,k])
    return listijk

if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    listijk=functionn(x,y,z,n)
    print(listijk)
