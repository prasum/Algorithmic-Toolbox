# Uses python2
import sys
import math
a=[]
keys=[]
def binary_search(a,x,p,q):
    
    left, right = p, q
    mid=math.floor(left+(right-left)/2.0)
    mid=int(mid)
    if(left>right):
        return -1
    else:
        if x==a[mid]:
            return mid
        elif x<a[mid]:
            return binary_search(a,x,left,mid-1)
        elif x>a[mid]:
            return binary_search(a,x,mid+1,right)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    a=[]
    keys=[]
    d = raw_input()
    data = d.split()
    for i in xrange(len(data)):
        data[i]=int(data[i])
    for j in xrange(1,len(data)):
        a.append(data[j])
    #print a
    e=raw_input()
    data1=e.split()
    for k in xrange(len(data1)):
        data1[k]=int(data1[k])
    for m in xrange(1,len(data1)):
        keys.append(data1[m])
    #print keys
    for l in xrange(len(keys)):
        print binary_search(a,keys[l],0,len(a)-1),
        