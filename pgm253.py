# biggest number of the elements of the arbitary aruguments
def num(*a):
    b=0
    for i in a:
     if i>b:
       b=i
    return b   
#main
l=num(1,2,3,4,5,6,7,8,9,10,11)
print("biggest number of the elements:",l)