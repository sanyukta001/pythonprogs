n=int(input("Enter a number "))
c=n
s=0
while(c>0):
    d=c%10
    c=c//10
    f=1
    for i in range(1,(d+1)):
        f=f*i
    s=s+f
if(s==n):
    print("Strong Number")
else:
    print("Not Strong number")
    
