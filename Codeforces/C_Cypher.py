for _ in range(int(input())):
    w = int(input())
    a = [int(i) for i in input().split()]
    ans = []
    for i in range(w):
        x,s = input().split()
        num = a[i]
        for b in range(int(x)):
            if s[b] == 'U':
                num = (num - 1) % 10
            else:
                num = (num + 1) % 10
        ans.append(num)
    print(*ans)