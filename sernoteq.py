n=int(input("Enter the number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            continue
        print(i,j)
            
    