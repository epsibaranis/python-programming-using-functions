# sum of two numbers using default argument  tt

def sum (a=200,b=300):
    s=a+b
    return s
#main
print("sum of two numbers",sum(b=4000))
print("sum of two numbers",sum(b=5000,a=7000))
print("sum of two numbers",sum(a=5000))