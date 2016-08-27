# Uses python2
n=input()
m=raw_input()
a=m.split()
for i in xrange(len(a)):
    a[i]=int(a[i])
    
a.sort()

k=a[len(a)-1]*a[len(a)-2]
print k