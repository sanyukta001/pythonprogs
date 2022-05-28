n=int(input("Enter the number of terms"))
x=int(input("Enter the value of x"))
s=0
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+(x**i)/f
print(s)
