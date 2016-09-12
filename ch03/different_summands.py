# Uses python2
def optimal_summands(n):
	summands = []
	k=n
	l=1
	while(k>2*l):
			k=k-l
			summands.append(l)
			l=l+1
	if(k<=2*l):
			summands.append(k)
			return summands

if __name__ == '__main__':
    
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print x,
