a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
#using third variable
#c=a+b
#a=c-a
#b=c-a
#without using 3rd variable
#a=a+b
#b=a-b
#a=a-b
#using bitwise operator
a=a^b
b=a^b
a=a^b
print("the value of a is ",a)
print("the value of b is ",b)
