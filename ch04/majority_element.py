# Uses python2
import math
a=[]
def get_majority_element(a):
    i=0
    count=1
    major=0
    for i in xrange(1,len(a)):
        if a[major]==a[i]:
            count=count+1
        else:
            count=count-1
        if count==0:
            major=i
            count=1
   
    return a[major]
    
def check(a):
    c=get_majority_element(a)
    count=0
    b=int(math.floor((len(a))/2.0))
    for i in xrange(len(a)):
        if a[i]==c:
            count=count+1
    if count>b:
        return 1
    else:
        return 0
        
if __name__ == '__main__':
    l = int(input())
    j=raw_input()
    a=j.split()
    for i in xrange(len(a)):
        a[i]=int(a[i])
    print check(a)
