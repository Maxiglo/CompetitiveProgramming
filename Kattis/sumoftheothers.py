while True:
    try:
        a = list(map(int,input().split()))
        for n in a:
            if n ==sum(a)-n:
                tr = n
        print(tr)
    except EOFError:
        break

