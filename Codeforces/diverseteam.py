a,b = map(int,input().split())

l= [int(i) for i in input().split()]


if len(set(l))<b:
    print('NO')
else:
    print('YES')
    rep=[]
    s = set(l)
    for nombre in s :
        if len(rep)<b:
            rep.append(l.index(nombre)+1)
        else:
            break
    rep.sort()
    print(*rep)
    