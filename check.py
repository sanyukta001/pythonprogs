#####function definition example#####
#def factorial(n):
#    f=1
#    for i in range(1,n+1):
#        f=f*i
#   return f
#n=int(input("Enter the number "))
#print(factorial(n))
#####multiple argument function#####
def marks(**m):
    print(m)
    print("\n")
    print(m.items())
    return""
print(marks(phys=10,math=20,chem=40))
print(marks(p=12,m=21,c=123,com=1234,d=12345))
