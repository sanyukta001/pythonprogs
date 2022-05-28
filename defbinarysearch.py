#8. Write a program in Python to take n numbers as
#input and create a list and then find whether a specific
#element is present in the list or not using binary search.
def binarysearch(lb,ub,s):
    flag=0
    while(lb<=ub):
        mid=(lb+ub)//2
        if(s==list1[mid]):
            flag=1
            break
        elif(s>list1[mid]):
            lb=mid+1
        else:
            ub=mid-1
    if(flag==0):
        print("The number is not present")
    else:
        print("The number is present at index :", mid)
    
n=int(input("Enter the number of elements of the list : "))
list1=[]
for i in range(0, n):
    b=int(input("Enter a number : "))
    list1.append(b)
print(list1)
s=int(input("Enter the number to be searched : "))
binarysearch(0,n-1,s)
