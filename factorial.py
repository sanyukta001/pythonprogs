n=int(input("Enter the value of n"))
p=1
if(n<0):
    print("Invalid Input")
else:
    for i in range(1,(n+1)):
        p*=i
    print("factorial of ",n," is(for-loop) ",p)
j=1
f=1
while(j<=n):
    f*=j
    j+=1
print("factorial of ",n," is(while-loop) ",f)
