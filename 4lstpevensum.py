n=int(input("Enter the number of inputs: "))
l=[]
for i in range(0,n):
    b=int(input("Enter the value: "))
    l.append(b)
s=0
for i in range(0,n):
    if(l[i]%2==0):
        s=s+l[i]
print("The sum of all the evens numbers is: ",s)
