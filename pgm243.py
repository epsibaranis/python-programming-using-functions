# sum of two numbers using default argument
def sum (a=40,b=80):
    c=a+b
    return c
#main
n=int(input('n=?'))
m=int(input('m=?'))
x=sum()
print("sumof two integer\'s Default Arguments:",x)
y=sum(20)
print("sumof two integer\'s ",y)
z=sum(100,200)
print("sumof two integer\'s ",z)
x1=sum(n)
print("sumof two integer\'s",x1)
y1=sum(m,n)
print("sumof two integer\'s",y1)    