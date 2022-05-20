# product of the elements of the arbitary aruguments
def num(*a):
    c=1   
    for i in a:
       c=c*i
    return c
   
#main
l=num(1,2,3,4,5,6,7,8,9,10,11)
print("product of the elements:",l)