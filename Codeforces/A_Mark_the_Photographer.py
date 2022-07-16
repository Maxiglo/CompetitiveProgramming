for _ in range(int(input())):
    a,b = map(int, input().split())
    x = sorted([int(i) for i in input().split()])
    f = False 
    for i in range(a):
        if x[i+a] - x[i] < b:
            f = True
            break 
    print('YES' if not f else 'NO')

