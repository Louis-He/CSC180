def fibo(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def fibol(n):
    a=[]
    for i in range (0,n+1):
        a=a+[fibo(i)]
    return a

def redfibo(n):
    def product(a,b):
         return a*b
    return reduce(product,fibol(n))



