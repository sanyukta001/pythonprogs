def display(r,c,m):
    print("The elements of the matrix are ")
    for i in range(0,r):
        for j in range(0,c):
            print(m[i][j],end=" ")
        print("\n")

r=int(input("Enter the row "))
c=int(input("Enter the column "))
m=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        b=int(input("Enter the value: "))
        n.append(b)
    m.append(n)
display(r,c,m)
m1=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        b=int(input("Enter the vaue: "))
        n.append(b)
    m1.append(n)
display(r,c,m1)
s=[]
for i in range(0,r):
    e=[]
    for j in range(0,c):
        f=m[i][j]+m1[i][j]
        e.append(f)
    s.append(e)
display(r,c,s)
