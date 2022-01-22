for _ in range(int(input())):
    n,k = map(int,input().split())
    a= [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    r = sorted(zip(a,b), key = lambda x:x[0])
    for i in r:
        if i[0]<=k:
            k+=i[1]
    print(k)