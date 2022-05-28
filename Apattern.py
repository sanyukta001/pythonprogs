n=int(input("Enter the number of rows "))
for i in range(1,n+1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        if(j==1 or i==j or i==((n+1)//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#include<iostream>
#using namespace std;
#int main(){
#   int n;
#   cout<<"Enter the number of rows "<<endl;
#   cin>>n;
#  for(int i=1;i<=n;i++)
#   {
#      for(int j=1;j<=n+1-i;j++)
#      cout<<" ";
#      for(int j=1;j<=i;j++)
#      {
#      if(j==1 || j==i || i==((n+1)/2))
#        cout<<" *";
#      else
#      cout<<"  ";
#      }
#      cout<<"\n";
#   }
#}
