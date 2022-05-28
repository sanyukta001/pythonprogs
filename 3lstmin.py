lst=[]
n=int(input("Enter the number of inputs "))
k=0
for i in range(0,n):
    k=int(input("Enter the value: "))
    lst.append(k)
min1=lst[0]
for i in range(0,n):
    if(lst[i]<min1):
        min1=lst[i]
print("minimum without using standard function is ",min1)
print("minimum using standard function ",min(lst))
