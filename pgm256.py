# count the +ve number,-ve number,zeroes in the n-random list using function
import random
def construct(n):    
    a=[random.randint(-100,100)for i in range(n)]
    return a
def number(a):
    x=0
    y=0
    z=0
    for i in a:
        if i>0:
            x=x+1
        elif i<0:
            y=y+1
        else:
            z=z+1 
    return x,y,z   
#main
n=int(input('n=?'))
a=construct(n)
print("list of random numbers:",a)
b=number(a)
print("count the +ve number,-ve number,zeroes in the n-random list using function",b)