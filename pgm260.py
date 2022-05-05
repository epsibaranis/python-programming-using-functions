# Intechange the seond biggest and second smallest in the list using function and global varibles
import random
b1=0
b2=0
s1=9999999
s2=9999999
def construct(n):    
    a=[random.randint(-100,100)for i in range(n)]
    return a
def interchange(a,n):
  global b1,b2,s1,s2
  for i in range(n):
    b1=a[i] if a[i]>b1 else b1
    s1=a[i] if a[i]<s1 else s1
    if a[i]!=b1:
      if a[i]>b2:
        b2=a[i]
        p1=i
    if a[i]!=s1:
     if a[i]<s2:
        s2=a[i]
        p2=i
  a[p1]=s2
  a[p2]=b2
def printlist(a,n):
    for i in range(n):
         print(a[i],end=('  '))
    print()
#main
n=int(input('n=?'))
a=construct(n)
print(a)
interchange(a,n)   
printlist(a,n)
