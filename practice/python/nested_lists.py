if __name__ == '__main__':
    grades=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([score,name])
    grades.sort()
    
    lowest=sum(x.count(grades[0][0]) for x in grades)
    del grades[:lowest]
    
    lowestSecond=sum(x.count(grades[0][0]) for x in grades)
    secondGrades=grades[:lowestSecond]
    
    print(*(list(list(zip(*secondGrades))[1])), sep = "\n") 
