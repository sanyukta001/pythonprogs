n=int(input("Enter the value of n: "))
s=0
for i in range(1,(n+1)):
    if(i%2!=0):
        s=s+i
print("sum of odd numbers for for-loop ",s)
j=1
s1=0
while(j<=n):
    if(j%2!=0):
        s1=s1+j
    j=j+1
print("sum of odd numbers for while-loop ",s1)
