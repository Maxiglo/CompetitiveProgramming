for _ in range(int(input())):
    a,b,c,x,y = map(int, input().split())
    rest = max((x-a), 0)+ max((y-b), 0)
    print('YES' if rest <= c else 'NO') 