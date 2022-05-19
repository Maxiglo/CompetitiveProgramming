for _ in range(int(input())):
    n = input()
    if len(n) == 2:
        print(n[1])
    else:
        print(min(map(int,list(n))))

