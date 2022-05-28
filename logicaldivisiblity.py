n=int(input("Enter a number: "))
if(n%4==0 and n%7==0):
    print("Number is disible by both 4 and 7")
elif(n%7==0 and n%4!=0):
    print("Number is divisible by 7 but not by 4")
elif(n%4==0 and n%7!=0):
    print("Number is divisible by 4 but not by 7")
else:
    print("Number is neither divisible by 4 nor 7")
