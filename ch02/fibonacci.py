# Uses python2
def calc_fib(n):
    fib=[]
    fib.append(0)
    fib.append(1)
    if(n>=2):
        for i in xrange(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
        return fib[i]
    elif(n==1):
        return 1
    else:
        return 0

n = int(input())
print(calc_fib(n))
