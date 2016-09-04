# Uses python2


def gcd_naive(a, b):
    if(b==0):
        return a
    else:
        return gcd_naive(b,a%b)

def lcm_naive(a, b):
    y=(a*b)/gcd_naive(a,b)
    return y
    

if __name__ == '__main__':
    m=raw_input()
    k=m.split()
    a=int(k[0])
    b=int(k[1])
    print(lcm_naive(a, b))

