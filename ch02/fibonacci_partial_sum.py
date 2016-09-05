# Uses python2
import sys

cache = {0: 0, 1: 1}

def fib_m(n):
    if n>60:
        n=n%60
    if n in cache:
            return cache[n]

    if n % 2 == 0:
            fib_half_n = fib_m(n // 2)
            result = (2 * fib_m(n // 2 - 1) + fib_half_n) * fib_half_n
    else:
            result = fib_m((n + 1) // 2) ** 2 + fib_m((n - 1) // 2) ** 2

    cache[n] = result
    return result
    
def get_fibonacci_last_digit_naive(n):
    
    a=2
  
    
    if(n>=2):
        
            
        if int(n)>60:
            if int(n)-60<=60:
                return fib_m(int(n)-60)%10
            elif int(n)-60>60:
                while int(n)-60*a>60:
                             a=a+1
                y=int(n)-60*a
                return fib_m(y)%10
        
        elif int(n)<=60:
            return fib_m(int(n))%10
        elif(n==1):
            return 1
        elif(n==0):
            return 0

def fibonacci_sum(f,to):
    j=[]
    sum=0
    j.append(0)
    j.append(1)
    for i in xrange(f,int(to)+1):
        m=i
        m=m%60
        sum=sum%10+get_fibonacci_last_digit_naive(str(m))%10
        
    return sum%10

if __name__ == '__main__':
    
    n=raw_input()
    k=n.split()
    for i in xrange(len(k)):
        k[i]=int(k[i])
    f=k[0]
    to=k[1]
    if(f>60):
        f=f%60
    if(to>60):
        to=to%60
    print(fibonacci_sum(f,to))