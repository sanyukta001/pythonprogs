m=int(input("Input the total marks"))
if(m>100):
    print("Invalid Input")
elif(m<0):
    print("Invalid Input")
elif(m>=90):
    print("Grade is Outstanding")
elif(m>=80):
    print("Grade is Excellent")
elif(m>=70):
    print("Grade is Fine")
elif(m>=60):
    print("Grade is Good")
elif(m>=50):
    print("Grade is Average")
elif(m>=40):
    print("Grade is Just pass")
elif(m>=0):
    print("Grade is Fail")
else:
    print("Invalid Input")
