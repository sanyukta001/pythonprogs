a=int(input("Enter the lower bound "))
b=int(input("Enter the upper bound "))
for i in range(a,b+1):
    s=0
    for j in range(1,((i//2)+1)):
        if(i%j==0):
            s=s+j
    if(s==i):
        print(i)
