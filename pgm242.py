# Biggest of three numbers using function
def biggest(a,b,c):
    d=(a if a>c else c)if a>b else (b if b>c else c)
    return d
#main
a=int(input('a=?'))
b=int(input('b=?'))
c=int(input('c=?'))
d=biggest(a,b,c)
print("Biggest of three Integer\'s using function:",d)