n=int(input("Enter the number of inputs: "))
l=[]
for i in range(0,n):
    b=int(input("Enter the value: "))
    l.append(b)
print("The maximum element is: ",max(l))
print("The minimum element is: ",min(l))
