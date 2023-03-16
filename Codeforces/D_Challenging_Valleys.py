for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    
    c = 0
    i = 0
    while i < n:
        j = i
        while j + 1 < n and l[j + 1] == l[i]:
            j += 1
        if (i == 0 or l[i - 1] > l[i]) and (j == n - 1 or l[j + 1] > l[j]):
            c += 1
        i = j + 1
    if c == 1:
        print("YES")
    else:
        print("NO")