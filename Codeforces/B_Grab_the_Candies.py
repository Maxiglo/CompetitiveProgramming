for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    z = sum(i for i in l if i%2==0)
    y = sum(i for i in l if i%2!=0)
    if z>y:
        print('YES')
    else:
        print('NO')