l=[]
print("Enter the list elements")
y=1
while(y==1):
    a=int(input())
    l.append(a)
    y=int(input("Enter 1 for entering next element and 0 for stopping"))
t=0
for i in range(0,len(l)):
    if(l[i]==l[4]):
        t+=1
if(len(l)==8 and t==3):
    print("True")
else:
    print("False")