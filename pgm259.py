# Intechange the Biggest and smallest in the list using function and global varibles
import random
b=0
s=9999999
def construct(n):    
    a=[random.randint(-100,100)for i in range(n)]
    return a
def interchange(a,n):
  global b,s
  for i in range(n):
    if a[i]>b:
        b=a[i]
        p=i
    if a[i]<s:
        s=a[i]
        q=i
  a[p]=s
  a[q]=b
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

