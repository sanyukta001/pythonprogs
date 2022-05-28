xs=int(input("Enter the value of x for sin "))
ns=int(input("Enter the number the terms for sin "))
x1s=(3.14285*xs)/180
s1=0
k1=0
for i in range(1,ns+1,2):
    p=x1s**i
    f=1
    for j in range(1,i+1):
        f=f*j
    s1=s1+((-1)**k1)*(p/f)
    k1+=1
print("sin",xs,round(s1,3))

x=int(input("Enter the value of x for cos "))
n=int(input("Enter the number the terms for cos "))
x1=(3.14285*x)/180
s=0
k=0
for i in range(0,n+1,2):
    p1=x1**i
    f1=1
    for j in range(1,i+1):
        f1=f1*j
    s=s+((-1)**k)*(p/f)
    k+=1
print("cos",x,round(s,3))

