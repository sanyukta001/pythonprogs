a=int(input("Enter a lower range "))
b=int(input("Enter a upper range "))
for i in range(a,b+1):
    c=i
    s=0
    while(c>0):
        d=c%10
        c=c//10
        f=1
        for j in range(1,(d+1)):
            f=f*j
        s=s+f
    if(s==i):
        print(i)
