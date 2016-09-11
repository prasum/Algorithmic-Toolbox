# Uses python2

a=[]
v=[1,5,10]
c=0
def get_change(m):
    c=0
    j=sorted(v,reverse=True)
    #print j
    for i in xrange(len(j)):
        if m==j[i]:
            c=c+1
            return c
        elif m>j[i]:
            while(m>j[i]):
                m=m-j[i]
                c=c+1
            if m==j[i]:
                c=c+1
                return c
        
       
            
            
    

if __name__ == '__main__':
    m = int(input())
    print get_change(m)
