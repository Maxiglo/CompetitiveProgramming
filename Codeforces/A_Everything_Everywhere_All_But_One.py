for _ in range(int(input())):
    l = int(input())
    a = sorted(map(int, input().split()))
    if len(set(a)) == 1:
        print('YES')
        continue 
    for i in range(l):
        if (sum(a) - a[i]) / (l - 1) == a[i]:
            print("YES")
            break
    else:
        print("NO")