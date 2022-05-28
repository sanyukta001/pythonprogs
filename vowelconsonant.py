s=input("Enter the string: ")
c=0
v=0
for i in range(0,len(s)):
    if(s[i].isalpha()):
        if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
            v+=1
        else:
            c+=1
print("The number of vowels is ",v)
print("The number of consonants is ",c)

