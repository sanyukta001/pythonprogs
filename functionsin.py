def power(x1s,i):
    return (x1s**i)
def factorial(i):
    f=1
    for j in range(1,i+1):
        f=f*j
    return f
xs=int(input("Enter the value of x for sin "))
ns=int(input("Enter the number the terms for sin "))
x1s=(3.14285*xs)/180
s1=0
k1=0
for i in range(1,ns+1,2):
    s1=s1+((-1)**k1)*(power(x1s,i)/factorial(i))
    k1+=1
#for i in range(1,ns+1,2):
#    p=x1s**i
#    f=1
#    for j in range(1,i+1):
#        f=f*j
#    s1=s1+((-1)**k1)*(p/f)
#    k1+=1
print("sin",xs,round(s1,3))
