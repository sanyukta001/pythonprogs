n=input("Enter the string ")
v=0
c=0
for i in range(0,len(n)):
    if(n[i]=='a'or n[i]=='e'or n[i]=='i'or n[i]=='o'or n[i]=='u'):
        v+=1
    else:
        c+=1
print("The number of vowels are",v,"and the number of consonents are",c)
