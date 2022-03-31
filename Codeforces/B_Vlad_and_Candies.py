for _ in range(int(input())):
    n = int(input()) # n types
    a = sorted([int(i) for i in input().split()]) # types

    if n == 1:
        if a[0] == 1:
            print('YES')
        else:
            print('NO')
    else:
        if abs(a[-1] - a[-2])  <= 1:
            print('YES')
        else:
            print('NO')   

        