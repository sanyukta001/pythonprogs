n=int(input("Enter the range: "))
l1=[]
l2=[]
a=0
b=1
if(n%2==0):
    n1=n//2
    n2=n//2
elif(n%2!=0):
    n1=(n+1)//2
    n2=(n-1)//2
for i in range(0,n1):
    if(i==0):
        l1.append(0)
    if(i==1):
        l1.append(1)
    else:
        c=a+b
        l1.append(c)
        a=b
        b=c
count=0
k=2
while(count!=n2):
    c=0
    for i in range(2,(k//2)+1):
        if(k%i==0):
            c+=1
    if(c==0):
        l2.append(k)
        count+=1
    k+=1
l=[]
k1=0
k2=0
for i in range(0,n):
    if(i%2==0):
        l.append(l1[k1])
        k1+=1
    else:
        l.append(l2[k2])
        k2+=1
print(l)
