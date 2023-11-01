for _ in range(int(input())):
    n = int(input())
    x = [int(i) for i in input().split()]
    rep = 0 
    temp = 0
    for c in x:
        if c==0:
            temp+=1
        else:
            rep = max(rep, temp)
            temp = 0
    rep=max(rep, temp)
    print(rep)