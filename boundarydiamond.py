n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        if(j==1 or j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,n+1-i):
        if(j==1 or j==n-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
