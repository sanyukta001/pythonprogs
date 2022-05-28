n1=input("Enter the first string ")
n2=input("Enter the second string ")
n3=input("Enter the third string ")
for i in range(0,len(n1)):
    if(n1[i]=='a'or n1[i]=='e'or n1[i]=='i'or n1[i]=='o'or n1[i]=='u'or n1[i]=='A'or n1[i]=='E'or n1[i]=='I'or n1[i]=='O'or n1[i]=='U'):
        n1=n1.replace(n1[i],'*')
print("updated first string ",n1)
for i in range(0,len(n2)):
    if(n2[i]!='a'and n2[i]!='e'and n2[i]!='i'and n2[i]!='o'and n2[i]!='u'and n2[i]!='A'and n2[i]!='E'and n2[i]!='I'and n2[i]!='O'and n2[i]!='U'):
        n2=n2.replace(n2[i],'$')
print("Updated second string ",n2)
for i in range(0,len(n3)):
    if(n3[i].isalpha()==True and n3[i].isupper()==True):
        n3=n3.replace(n3[i],n3[i].lower())
print("Updated third string ",n3)

      
