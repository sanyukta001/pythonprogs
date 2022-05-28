def display(r,c,m):
    print("The elements of the matrix are ")
    for i in range(0,r):
        for j in range(0,c):
            print(m[i][j],end=" ")
        print()

r1=int(input("Enter the row of first matrix "))
c1=int(input("Enter the column of first matrix "))
r2=int(input("Enter the row of second matrix "))
c2=int(input("Enter the column of second matrix "))
if(c1!=r2):
    print("Matrix multiplication not possible ")
else:
    m=[]
    print("Enter the elements of first matrix:")
    for i in range(0,r1):
        n=[]
        for j in range(0,c1):
            b=int(input("Enter the value: "))
            n.append(b)
        m.append(n)
    display(r1,c1,m)
    m1=[]
    print("Enter the elements of second matrix:")
    for i in range(0,r2):
        n=[]
        for j in range(0,c2):
            b=int(input("Enter the value: "))
            n.append(b)
        m1.append(n)
    display(r2,c2,m1)
    s=[]
    for i in range(0,r1):
        e=[]
        for j in range(0,c2):
            f=0
            for k in range(0,r2):
                f=f+(m[i][k]*m1[k][j])
            e.append(f)
        s.append(e)
    display(r1,c2,s)
