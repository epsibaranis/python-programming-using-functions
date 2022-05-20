#Biggset of three numbers
def biggest(a=7000,b=15000,c=400):
    d=(a if a>c else c)if a>b else (b if b>c else c)
    return d
#main
print("Biggset of three numbers",biggest(a=9000))
print("Biggset of three numbers",biggest(b=6000))
print("Biggset of three numbers",biggest(c=16000))