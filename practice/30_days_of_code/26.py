# Enter your code here. Read input from STDIN. Print output to STDOUT
#day month year format
returnedDate=list(map(int,input().split(' ')))
dueDate=list(map(int,input().split(' ')))

#decimal format of date for easy first compare
retFloat=(returnedDate[0]/31+returnedDate[1])/12+returnedDate[2]
dueFloat=(dueDate[0]/31+dueDate[1])/12+dueDate[2]

#logic
if retFloat<=dueFloat:
    fine=0
elif returnedDate[1]==dueDate[1]: #same month
    fine=15*(returnedDate[0]-dueDate[0])
elif returnedDate[2]==dueDate[2]: #same year
    fine=500*(returnedDate[1]-dueDate[1])
else:
    fine=10000
    
print(fine)
