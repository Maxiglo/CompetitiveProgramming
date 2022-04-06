m = int(input())
for case in range(m):
    c1,m1,y1,k1 = [int(i) for i in input().split()]
    c2,m2,y2,k2 = [int(i) for i in input().split()]
    c3,m3,y3,k3 = [int(i) for i in input().split()]
    c = min(c1,c2,c3)
    m = min(m1,m2,m3)
    y = min(y1,y2,y3)
    k = min(k1,k2,k3)
    tot = c + m + y + k 
    if tot < 1000000:
        print(f'Case #{case+1}: IMPOSSIBLE')
    else:
        trop = tot - 1000000
        rep = [c,m,y,k]

        for elem in range(len(rep)):
            if trop == 0:
                break
            if rep[elem] >= trop:
                rep[elem]-=trop
                trop = 0
            else:
                trop -= rep[elem]
                rep[elem] = 0     
        x = ' '.join(map(str,rep))    
        print(f'Case #{case+1}: {x}')
