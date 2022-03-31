for _ in range(int(input())):
    a,b = map(int, input().split())
    if b == 0:
        print(a+1)
    elif a == 0:
        print(1)
    else:
        print(2*b+a+1)