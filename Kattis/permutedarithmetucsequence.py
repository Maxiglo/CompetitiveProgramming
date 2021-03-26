n = int(input())

for i in range(n):
    l=[int(i) for i in input().split()]
    del l[0]
    dist=[]
    for j in range(len(l)-1):
        dist.append(abs(l[j]-l[j+1]))
    if len(set(dist))==1:
        print('arithmetic')
    else:
        l = sorted(l)
        dist=[]
        for k in range(len(l)-1):
            dist.append(abs(l[k]-l[k+1]))
        if len(set(dist))==1:
            print('permuted arithmetic')
        else:
            print('non-arithmetic')
        
