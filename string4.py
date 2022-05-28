#method1
n=input("Enter the string ")
if(n[::-1]==n):
    print("Palindrome ")
else:
    print("Not Palindrome ")
#method2
w=""
for i in range(0,len(n)):
    w=n[i]+w
if(w==n):
    print("Palindrome ")
else:
    print("Not Palindrome ")
    
