n=int(input("Enter a number "))
flag=1
i=2
while(i<=(n//2)):
    if(n%i==0):
        flag=0
        break
    else:
        i+=1
if(flag==1):
    print("YES it is PRIME")
else:
    print("NO it is NOT PRIME ")
