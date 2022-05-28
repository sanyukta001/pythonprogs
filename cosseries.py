x=int(input("Enter the value of x"))
n=int(input("Enter the number the terms"))
x1=(3.14285*x)/180
s=0
k=0
for i in range(0,n+1,2):
    p=x1**i
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+((-1)**k)*(p/f)
    k+=1
print(round(s,3))
