num=int(input("Enter a number "))
r=0
n=num
while(n>0):
    d=n%10
    n=n//10
    r=r*10+d
if(r==num):
    print("yes it is palindrome")
else:
    print("no it is not palindrome")
