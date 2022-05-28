t=int(input("Enter the number of testcases "))
f=0
while(t>0):
    t=t-1
    a=input()
    b=input()
    a=a.upper()
    b=b.upper()
    if(len(a)!=len(b)):
        f=1
    else:
        s1=[]
        s2=[]
        k=len(a)
        for i in range(0,len(a)):
            s1.append(a[i])
            s2.append(b[i])
        for i in range(0,k):
            m=s1[i]
            if(m in s2):
                s1.remove(m)
                s2.remove(m)
                k=k-1
                i-=1
            else:
                f=1
                break
    if(f==1):
        print("NO")
    else:
        print("YES")
    
    
