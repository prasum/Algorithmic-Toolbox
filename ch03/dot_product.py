#Uses python2

import sys

def max_dot_product(a, b):
    c=sorted(a,reverse=True)
    d=sorted(b,reverse=True)
    #print c
    #print d
    res = 0
    for i in range(len(c)):
        res += c[i] * d[i]
    return res

if __name__ == '__main__':
    
    data = raw_input()
    m=data.split()
    n = int(m[0])
    k=raw_input()
    a=k.split()
    for i in xrange(len(a)):
        a[i]=int(a[i])
    l=raw_input()
    b=l.split()
    for j in xrange(len(b)):
        b[j]=int(b[j])
    print(max_dot_product(a, b))