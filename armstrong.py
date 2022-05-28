n=int(input("Enter the number "))
cnt=0
cp=n
while(cp>0):
    cnt+=1
    cp=cp//10
c=n
s=0
while(c>0):
    s=s+((c%10)**cnt)
    c=c//10
if(s==n):
    print("Armstrong number")
else:
    print("Not Armstrong number")
