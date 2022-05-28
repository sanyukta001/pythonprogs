n=int(input("Enter the number of rows"))
l=1
for i in range(1,n+1):
    for k in range(n,i-1,-1):
        print("  ",end="")
    for j in range(1,i+1):
        print(l,"  ",end="")
        l+=1
    print("\n")
