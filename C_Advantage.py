for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    m = max(l)
    m2 = sorted(l)[-2]
    rep = []
    for c in l:
        if c != m:
            rep.append(c-m)
        else:
            rep.append(c-m2)

    print(*rep)