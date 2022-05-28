def power(x1s,i):
    return (x1s**i)
def factorial(i):
    f=1
    for j in range(1,i+1):
        f=f*j
    return f
xs=int(input("Enter the value of x for cos "))
ns=int(input("Enter the number the terms for cos "))
x1s=(3.14285*xs)/180
s1=0
k1=0
for i in range(0,ns+1,2):
    s1=s1+((-1)**k1)*(power(x1s,i)/factorial(i))
    k1+=1
print("cos",xs,round(s1,3))
