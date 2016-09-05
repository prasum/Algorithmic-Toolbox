# Uses python2
import sys

def get_fibonacci_last_digit_naive(n):
    fib=[]
    a=2
    fib.append(0)
    fib.append(1)
    if(n>=2):
        for i in xrange(2,61):
            fib.append(fib[i-1]+fib[i-2])
        if int(n)>60:
            if int(n)-60<=60:
                return fib[int(n)-60]%10
            elif int(n)-60>60:
                while int(n)-60*a>60:
                             a=a+1
                y=int(n)-60*a
                return fib[y]%10
        
        elif int(n)<=60:
            return fib[int(n)]%10
        elif(n==1):
            return 1
        elif(n==0):
            return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
