a=int(input("Enter the lower range "))
b=int(input("Enter the upper range "))
for i in range(a,(b+1)):
    c=0
    for j in range(2,((i//2)+1)):
        if(i%j==0):
            c+=1
    if(c==0):
        print(i)
