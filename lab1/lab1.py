def summl(n):
    r=0
    Neg=True
    for i in range(1,n+1):
        if Neg:
            r=r-i
            Neg=False
        else:
            r=r+i
            Neg=True
    return r


def mult(A,B):
   r=1
   for i in range(0,B):
     r=r*A
     i=i+1
   return r
