for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    d, zero = set(), []
    ans = 'YES'
    for i in range(len(a)):
        diff = a[i] - b[i]
        if diff < 0:
            ans = 'NO'
            break
        if b[i] > 0:
            d.add(diff)
        else:
            zero.append(diff)
    if d and zero:
        if len(d) > 1 or max(zero) > max(d):
            ans = 'NO'
    elif d and not zero:
        if len(d) > 1:
            ans = 'NO'
    print(ans)