#Uses python2

def largest_number(x):
    maxlen = len(str(max(x)))
    return ''.join(sorted((str(v) for v in x), reverse=True,
                          key=lambda i: i*(maxlen * 2 // len(i))))
    
    

if __name__ == '__main__':
    n=input()
    data = raw_input()
    a=data.split()
    for i in xrange(len(a)):
        a[i]=int(a[i])
        
        
    print largest_number(a)