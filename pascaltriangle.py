r=int(input("Enter the no.of rows: "))
l=[]
for i in range(0,r+1):
    b=[]
    for j in range(0,r+1):
        b.append(0)
    l.append(b)
for i in range(0,r+1):
    for j in range(0,i+1):
        if(j==0 or j==i):
            l[i][j]=1
        else:
            l[i][j]=l[i-1][j-1]+l[i-1][j]
for i in range(0,r+1):
    for j in range(0,(r-i+1)):
        print(end=" ")
    for k in range(0,i+1):
        print(l[i][k],end=" ")
    print()
        
