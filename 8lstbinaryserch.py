l1=[]
n=int(input("Enter the number of elements "))
k=0
for i in range(0,n):
    k=int(input("Enter the value: "))
    l1.append(k)
s=int(input("Enter the element to be searched "))
lb=0
ub=n-1
mid=0
f=0
while(lb<=ub):
    mid=(lb+ub)//2
    if(l1[mid]==s):
        f=1
        break
    elif(s<l1[mid]):
        ub=mid-1
    else:
        lb=mid+1
if(f==1):
    print("YES PRESENT", "at index",mid)
else:
    print("NOT PRESENT")        
