n=input("Enter the String ")
#method1
print(n[::-1])
#method2
r=""
for i in range(len(n)-1,-1,-1):
    r=r+n[i]
print(r)
