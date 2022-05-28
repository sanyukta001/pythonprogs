l1=[]
n=int(input("Enter the number of elements "))
k=0
for i in range(0,n):
    k=int(input("Enter the value: "))
    l1.append(k)
s=int(input("Enter the element to be searched "))
index=0
f=0
for i in range(0,n):
    if(l1[i]==s):
        f=1
        index=i
        break
if(f==1):
    print("YES PRESENT"," at index",index)
else:
    print("NOT PRESENT")
    
