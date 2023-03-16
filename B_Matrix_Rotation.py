for _ in range(int(input())):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    l = [[a,b,c,d], [c,a,d,b], [d,c,b,a], [b,d,a,c]]
    f = 0
    for i in l:
        if i[0]<i[1] and i[2]<i[3] and i[0]<i[2] and i[1]<i[3]:
            f=1
            break
    print('NO' if not f else 'YES')