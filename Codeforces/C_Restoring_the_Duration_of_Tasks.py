for _ in range(int(input())):
    x = int(input())
    s = [int(i) for i in input().split()]
    f = [int(i) for i in input().split()]

    t = -10**10
    temps = []
    for i in range(x):
        temps.append(min(f[i] - s[i], f[i] - t))
        t = f[i]
    print(*temps)
