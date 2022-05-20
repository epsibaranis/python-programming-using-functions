# consruct a list of n-random numbers for a function and return itr and print it element by element
import random
def construct(n):    
    a=[random.randint(0,100)for i in range(n)]
    return a
def num(a):
    for i in a:
        print(i)
#main
n=int(input('n=?'))
a=construct(n)
print("print the list element one by one:",a)
num(a)