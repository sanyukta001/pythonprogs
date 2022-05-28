def binarysearch(lb,ub,s):
        mid=(lb+ub)//2
        if(s==l[mid]):
            return mid
        if(lb>ub):
            return -1
        elif(s>l[mid]):
            return binarysearch(mid+1,ub,s)
        else:
            return binarysearch(lb,mid-1,s)
n=int(input("Enter the number of elements of the list : "))
l=[]
for i in range(0, n):
    b=int(input("Enter a number : "))
    l.append(b)
print(l)
s=int(input("Enter the number to be searched : "))
x=binarysearch(0,n-1,s)
if(x==-1):
    print("Element not present ")
else:
    print("Element is preset at ",x)
    

