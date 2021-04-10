# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
book = {}
for _ in range(n):
    number=list(input().split(" "))
    book.update({number[0]:number[1]})
    
while True:
    try:
        query=input()
    except EOFError:
        break
    
    if query==[]:
        break
    elif query in book:
        print(str(query)+"="+str(book[query]))
    else:
        print("Not found")
