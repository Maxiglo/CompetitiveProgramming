for _ in range(int(input())):
    n,k = map(int, input().split())
    l = [int(i) for i in input().split()]
    ll = sorted([- l[i] + (n - 1 - i) for i in range(n)])
    base = sum(l)
    poss = [base]
    for i in range(k):
        base += ll[i] - i
        poss.append(base)
    print(min(poss))
