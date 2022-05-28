lst=[]
n=int(input("Enter the number of inputs "))
k=0
sum=0
for i in range(0,n):
    k=int(input("Enter the value: "))
    lst.append(k)
print("The list is: ",lst)
for i in range(0,n):
    sum=sum+lst[i]
print("sum is ",sum)
