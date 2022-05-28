def gcd(a,b):
    if((a%b)==0):
        return a
    else:
        return gcd((a%b),a)
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
print("GCD of two numbers are ",gcd(a,b))
c=int(input("Enter the third number "))
print("GCD of two numbers are ",gcd(c,gcd(a,b)))
