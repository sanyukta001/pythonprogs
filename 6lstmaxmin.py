lst=[]
n=int(input("Enter the number of inputs "))
k=0
for i in range(0,n):
    k=int(input("Enter the value: "))
    lst.append(k)
max1=lst[0]
min1=lst[0]
for i in range(0,n):
    if(lst[i]>max1):
        max1=lst[i]
    if(lst[i]<min1):
        min1=lst[i]
print("maximum number is ",max1)
print("minimum number is ",min1)
