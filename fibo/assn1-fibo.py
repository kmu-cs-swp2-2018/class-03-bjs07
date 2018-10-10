import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    last,tmp=1,1
    if n<=1:
        return n
    else:
        for i in range(n-1):
            last,tmp=tmp,last+tmp

        return last




while True:
        nbr = int(input("Enter a number: "))
        if nbr == -1:
                break
        ts = time.time()
        fibonumber = iterfibo(nbr)
        ts = time.time() - ts
        print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
        ts = time.time()
        fibonumber = fibo(nbr)
        ts = time.time() - ts
        print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
