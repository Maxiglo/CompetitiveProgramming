for _ in range(int(input())):
    best_score = 0
    ans = 0
    for i in range(int(input())):
        a,b = map(int,input().split())
        if a <=10:
            if b > best_score:
                best_score = b
                ans = i+1
    print(ans)
            