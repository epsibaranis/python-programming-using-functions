#Biggset of three numbers
def biggest(a=7000,b=15000,c=400):
    d=(a if a>c else c)if a>b else (b if b>c else c)
    return d
#main
print(biggest(a=9000))
print(biggest(b=6000))
print(biggest(c=16000))

