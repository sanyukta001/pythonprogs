def maximum(a,b):
    if(a>b):
        return a
    else:
        return b
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
print("The maximum of two numbers are",maximum(a,b))
c=int(input("Enter the third number "))
print("The maximum of three numbers are",maximum(c,maximum(a,b)))
