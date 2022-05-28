l1=[]
k=0
s=0
n=int(input("Enter the number of elements"))
for i in range(0,n):
    k=int(input())
    l1.append(k)
for i in range(0,n):
    if(l1[i]%2==0):
        s=s+l1[i]
print("The sum of even numbers are ",s)
