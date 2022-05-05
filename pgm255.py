# construct a list of n-random numbers for a function and return it and print sum of the element

import random
def construct(n):    
    a=[random.randint(0,100)for i in range(n)]
    return a
def num(a):
    for i in a:
        print(i)
def num2(a):
    s=0
    for i in a:
        s=s+i
    return s
#main
n=int(input('n=?'))
a=construct(n)
print(a)
num(a)
print('sum of the element=',num2(a))