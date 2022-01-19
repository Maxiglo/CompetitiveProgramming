import bisect

n,q = map(int,input().split())

l = sorted([int(i) for i in input().split()])


for _ in range(q):
    x = int(input())
    print(n-bisect.bisect_left(l,x))

    
