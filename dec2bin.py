n=int(input("Enter the number "))
d=0
i=0
r=0
while(n!=0):
    d=n%2
    n=n//2
    r=r+d*(10**i)
    i+=1
print("The binary is",r)
