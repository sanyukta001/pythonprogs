
#a=int(input("Enter the number"))
#b=float(input("Enter another number"))
#c=int(a+b)
#print(c)
#l1=[[1,2],[3,4],[5,6],[7,8]]
#l2=l1
#print(l1)
#print(l2)
#l1[3][0]=700
#print(l1)
#print(l2)
import copy as c
l1=[[1,2],[3,4],[5,6],[7,8]]
l3=c.copy(l1)
l4=c.deepcopy(l1)
l3[2][0]=500
print(l1)
print(l3)
l4[1][0]=300
print(l1)
print(l4)
#import array as a
#l=[1,2,3,5,6]
#b=a.array('d',l)
#print(b)
#print(l)
# import NumPy as np
# l=[1,2,3,5]
# t=(1,2,3,5)
# a=np.array(l)
# b=np.array(t)
# print(l)
# print(t)
# print(a)
# print(b)
