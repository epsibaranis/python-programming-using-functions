#area of circle using default argumnet
def area(r=100):
    a=22/7*r**2
    return a
#main
n=int(input('n=?'))
print(area())
print(area(7))
print(area(n))
