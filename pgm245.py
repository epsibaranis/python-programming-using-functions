# Biggest of three numbers using default argument 
def Biggest(a=10,b=20,c=5):
    d=(a if a>c else c)if a>b else (b if b>c else c)
    return d
#main
x=int(input('x=?'))
y=int(input('y=?'))
z=int(input('z=?'))
print("Biggest of three Integer\'s",Biggest())
print("Biggest of three Integer\'s",Biggest(x))
print("Biggest of three Integer\'s",Biggest(x,y))
print("Biggest of three Integer\'s",Biggest(x,y,z))
print("Biggest of three Integer\'s",Biggest(80))
print("Biggest of three Integer\'s",Biggest(80,90))
print("Biggest of three Integer\'s",Biggest(80,90,100))