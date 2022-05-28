#Question 2.a
n=int(input("Enter the size of the list"))
l=[]
a=0
print("Enter the elements of the list ")
for i in range(0,n):
    a=int(input())
    l.append(a)
max1=l[0]
for i in range(0,n):
    if(l[i]>max1):
        max1=l[i]
print("maximum number Without using standard function",max1)

print("maximum number Using standard function:",max(l))
