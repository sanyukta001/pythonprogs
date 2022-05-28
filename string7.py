n1=input("Enter the first string ")
n2=input("Enter the second string ")
#method1
if(sorted(n1)==sorted(n2)):
    print("IT IS ANAGRAM ")
else:
    print("IT IS NOT ANAGRAM ")
#method2
if(len(n1)!=len(n2)):
    print("IT IS NOT ANAGRAM ")
else:
    f=0
    for i in range(0,len(n1)):
        if(n1.count(n1[i])!=n2.count(n1[i])):
            f=1
            break
    if(f==1):
        print("IT IS NOT ANAGRAM ")
    else:
        print("IT IS ANAGRAM ")
        
