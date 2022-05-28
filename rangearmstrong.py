a=int(input("Enter the lower range "))
b=int(input("Enter the upper range "))
for i in range(a,(b+1)):
    cnt=0
    cp=i
    while(cp>0):
        cnt+=1
        cp=cp//10
    c=i
    s=0
    while(c>0):
        s=s+((c%10)**cnt)
        c=c//10
    if(s==i):
        print(i)
