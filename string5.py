n=input("Enter the string ")
a=0
s=0
d=0
sc=0
for i in range(0,len(n)):
    if(n[i].isalpha()==True):
        a+=1
    elif(n[i].isspace()==True):
        s+=1
    elif(n[i].isdigit()==True):
        d+=1
    else:
        sc+=1
print("The number of alphabets is ",a)
print("The number of space is ",s)
print("The number of digit is ",d)
print("The number of special character is ",sc)
