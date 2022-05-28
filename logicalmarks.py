m=int(input("Input the total marks"))
if(m>100 or m<0):
    print("Invalid Input")
elif(m>=90 and m<=100):
    print("Grade is Outstanding")
elif(m>=80 and m<=89):
    print("Grade is Excellent")
elif(m>=70 and m<=79):
    print("Grade is Fine")
elif(m>=60 and m<=69):
    print("Grade is Good")
elif(m>=50 and m<=59):
    print("Grade is Average")
elif(m>=40 and m<=49):
    print("Grade is Just pass")
else:
    print("Grade is Fail")
