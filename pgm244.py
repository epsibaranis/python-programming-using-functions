#area of circle using default argumnet
def area(r=100):
    a=22/7*r**2
    return a
#main
n=int(input('n=?'))
print("Area of the circle:",area())
print("Area of the circle:",area(7))
print("Area of the circle:",area(n))