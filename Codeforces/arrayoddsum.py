n = int(input())

for i in range(n):
    a = int(input())
    ls= [int(i) for i in input().split()]
    somme = sum(ls)
    y= list(set(ls))
    ans = False
    for j in ls:
        for k in y:
            if (somme+(k-j))%2:
                ans = True
                break
        if ans:
            print('YES')
            break
    if not ans : 
        print('NO')