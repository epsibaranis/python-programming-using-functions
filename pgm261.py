# generate a menu in default argument 
import random
def menu():
    print('1:Create a matrix')
    print('2:print a matrix')
    print('3:print a taranfersmatrix')
    print('4:sum of the elements of the matrix in a row')
    print('5:Biggest element in the coloumn of a matrix')
    print('6:sum of two matrixes')
    print('7:product of two matrixes' )
    print(8)
    print(9)
    print(10)
    n=int(input('n=?'))  
    return n
def createMat():
    a=[[random.randint(0,10)for j in range(3)]for i in range(3)]
    return a
def printMat(b):
    for i in range(1):
        for j in range(3):
            print(b[j])
def printtranfersMat(b):
    for i in range(3):
        for j in range(3):
            print(b[j][i],end=(' '))
        print()
def sumrowsinMat(b):
    s=0
    q=[]
    for i in range(3):        
        for j in range(3):
          s=s+b[i][j]  
        q.append(s)
    return q 
def columnsBigelenmat(b):
    z=[]
    for i in range(3):
        l=0
        for j in range(3):
            l=b[j][i]if b[j][i]>l else l
        z.append(l)
    return z
def sumoftwoMat(b1,b2):
    h=[]
    for i in range(3):
        y=[]
        for j in range(3):
            s1=b1[i][j]+b2[i][j]
            y.append(s1)
        h.append(y)
    return h
def productoftwoMaat(b1,b2):
    p=[]
    for i in range(3):
        r=[]
        for j in range(3):
            g=0
            for k in range(3):
               g=g+b1[i][k]*b2[k][j]
            r.append(g)
        p.append(r)
    return p
#main
n=menu()
while n!=10:
      if n==1:
         b=createMat()
         print(b)
      elif n==2:
        b=createMat()
        printMat(b)
      elif n==3:
          b=createMat()
          print(b)
          printtranfersMat(b)
      elif n==4:
          b=createMat()
          print(b)
          t=sumrowsinMat(b)
          print(t)
      elif n==5:
          b=createMat()
          print(b)
          o=columnsBigelenmat(b)
          print(o)
      elif n==6:
          b1=createMat()
          b2=createMat()
          print(b1)
          print(b2)
          v= sumoftwoMat(b1,b2)
          print(v)
      elif n==7:
          b1=createMat()
          b2=createMat()
          print(b1)
          print(b2)
          w=productoftwoMaat(b1,b2)
          print(w)
          
      n=menu()
   