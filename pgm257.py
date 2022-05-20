# count the +ve number,-ve number,zeroes in the n-random list using global variables
import random
x=0
y=0
z=0
def construct(n):    
    a=[random.randint(-100,100)for i in range(n)]
    return a
def number(a):
    global z,x,y
    for i in a:
        if i%2==0:
            x=x+1
        elif i<0:
            y=y+1
        else:
            z=z+1          
#main
n=int(input('n=?'))
a=construct(n)
print("list",a)
number(a)
print("count the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variablescount the +ve number,-ve number,zeroes in the n-random list using global variables",z,x,y)