#Constut a list of n-andom numbersusing functin count th number that are diiviisible by 2,3,5,7 and 9 using lbal variable
import random
x=0
y=0
z=0
p=0
q=0
def construct(n):    
    a=[random.randint(-100,100)for i in range(n)]
    return a
def number(a):
    global x,y,z,p,q
    for i in a:
        if i%2==0:
            x=x+1
        elif i%3==0:
            y=y+1
        elif i%5==0:
            z=z+1
        elif i%7==0:
            p=p+1
        elif i%9==0:
            q=q+1
#main
n=int(input('n=?'))
a=construct(n)
print("list",a)
number(a)
print("Constut a list of n-andom numbersusing functin count th number that are diiviisible by 2,3,5,7 and 9 using lbal variable",x,y,z,p,q)