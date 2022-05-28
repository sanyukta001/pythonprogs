n=int(input("Enter a number "))
r=0
while(n>0):
    d=n%10
    n=n//10
    r=r*10+d
print("reverse of the number is ",r)
