a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
c=int(input("Enter the third number "))
if(a>b):
    if(a>c):
        print("a is greatest")
    else:
        print("c is greatest")
elif(b>c):
        print("b is greatest")
else:
    print("c is greatest")
