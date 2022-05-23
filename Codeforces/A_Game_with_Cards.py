for _ in range(int(input())):
    a = int(input())
    l = [int(i) for i in input().split()]
    b = int(input())
    l2 = [int(i) for i in input().split()]
    m = max(l)
    m2 = max(l2)
    if m == m2:
        print('Alice')
        print('Bob')
    else:
        if m > m2:
            print('Alice')
            print('Alice')
        elif m2 > m:
            print('Bob')
            print('Bob')