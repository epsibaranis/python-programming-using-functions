# sum of two numbers using default argument
def sum (a=40,b=80):
    c=a+b
    return c
#main
n=int(input('n=?'))
m=int(input('m=?'))
x=sum()
print(x)
y=sum(20)
print(y)
z=sum(100,200)
print(z)
x1=sum(n)
print(x1)
y1=sum(m,n)
print(y1)    