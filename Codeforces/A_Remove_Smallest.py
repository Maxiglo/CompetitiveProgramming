for _ in range(int(input())):
    x = int(input())
    l = sorted(list(set([int(i) for i in input().split()])))
    if len(l) == 0:
        print('YES')
        continue
    mdiff=0
    ok = 0
    for i in range(len(l)-1):
        if l[i+1]-l[i] > 1:
            print('NO')
            ok=1
            break
    if not ok:
        print('YES')



