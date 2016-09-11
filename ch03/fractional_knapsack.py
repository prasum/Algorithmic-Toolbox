# Uses python2
values=[]
weights=[]
c=[]
l={}
m={}
def get_optimal_value(capacity, weights, values):
    value =0.0
    # write your code here
    for i in xrange(len(weights)):
        c.append(values[i]/weights[i])
        l[weights[i]]=values[i]/weights[i]
        m[values[i]]=values[i]/weights[i]
    d=sorted(c,reverse=True)
    #print d
    #print l
    #print m
    for i in xrange(len(d)):
        a=l.keys()[l.values().index(d[i])]
        b=m.keys()[m.values().index(d[i])]
        if capacity==a:
            value=value+b
            
            return value
        elif capacity>a:
            capacity=capacity-a
            value=value+b
            
          
                
        else:
            value=value+d[i]*capacity
            
            return value
    return value


if __name__ == "__main__":
    data = raw_input()
    k = data.split()
    n=int(k[0])
    capacity=int(k[1])
    for i in xrange(n):
        g=raw_input()
        b=g.split()
        y=float(b[0])
        x=float(b[1])
        values.append(y)
        weights.append(x)
    opt_value = get_optimal_value(capacity, weights, values)
    
    print '%.3f' % opt_value