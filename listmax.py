def maximum(a,b):
    if(a>b):
        return a
    else:
        return b
l=[]
n=int(input("Enter the size of the list"))
for i in range(0,n):
    b=int(input())
    l.append(b)
m=0
for i in range(0,len(l)-1):
    m=maximum(l[i],maximum(l[i],l[i+1]))
print(m)
