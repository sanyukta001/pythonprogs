l=[]
k=0
n=int(input("Enter the number of elements"))
for i in range(0,n):
    k=int(input())
    l.append(k)
print("before sorting")
print(l)
for i in range(0,n):
    m=i
    for j in range(i+1,n):
        if(l[m]>l[j]):
            m=j
    t=l[i]
    l[i]=l[m]
    l[m]=t
print("after sorting")
print(l)
